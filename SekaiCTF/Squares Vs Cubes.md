# SQUARES VS CUBES (Cryptography)

### Challenge Description:

In this challenge, three 512-bit prime numbers, p, q, and r, are used to create a modulus N and an encryption scheme. The hidden flag is padded and incorporated into the encryption process. The challenge provides two types of values—squares and cubes derived from the prime numbers and padded flag. The objective is to recover the hidden flag by solving a set of polynomial equations.

### Code Analysis:

- p, q, r, are 512 bit primes.
- N = pqr = e
- d = modular inverse of e
- flag = 128 bytes
- value_for_genni = p^2 + (q + r*padded_flag)^2
- value_for_sbg = p^3 + (q + r*padded_flag)^3
- x0 = randbelow(N)
- x1 = randbelow(N)
- The challenge allows choosing between Genni's or SBG's value by providing a value v. The challenge then provides two decrypted values m0 and m1.
- m0 = (pow(v - x0, d, N) + value_for_genni) % N
- m1 = (pow(v - x1, d, N) + value_for_sbg) % N

### Approach:

I barely understood this, but mod math, so we try...

If we send x0 as v, we'll get:

```
m0 = p^2 + (q + rf)^2
m1 = p^3 + (q + rf)^3 + (x0 - x1)^d
```

Let q + rf = 𝜁.

```
x0 - x1 = (m1 - p^3 - 𝜁^3)^e
𝜁^2 - m0 ≡ 0 (mod p)
x0 - x1 + (𝜁^3 - m1)^e ≡ 0 (mod p)
```

Roots of both polynomials are 𝜁-(q+rf).

Solve for p - Use the greatest common divisor (GCD) to find p:

```
p = gcd(N,large polynomial expression)
```

Since we have p, qrf is easy to find.

```python
qrf = ZZ(-(polypow(𝜁**3 + p**3 - m1, N, 𝜁**2 + p**2 - m0) + x0 - x1).monic()[0])
```

Find q_approx:

```python
qr = N//p
q_approx = bytes_to_long(b'SEKAI{' + bytes(122)) * qr // qrf
```

q:
```python
y = Zmod(qr)['y'].gen()
q = ZZ((y*(y-qrf))(y=y+q_approx).small_roots(X = 2**464, epsilon=0.08)[0]) + q_approx
```

flag:
```python
print(long_to_bytes(qrf * q // qr))
```

### Flag:

`SEKAI{this_challenge_was_originally_called_oblivion_but_there_was_an_ACSC_crypto_also_called_that}`