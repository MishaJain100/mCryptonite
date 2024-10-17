# TCP15PRIME (Cryptography)

### Challenge Description:

plzz check my prime

### Given: 

- p == a^51 + 51*b^51, where p is prime.

### Approach used:

- Tried taking Fermat's Little Theorem by taking both sides modulo 51.
- p ≡ a^51 mod 51
- p ≡ a mod 51
- a = p % 51 + k * 51
- Bruteforce: Too computationally expensive
- Tried CRT by utilizing 17 and 3, then combining solutions, but that didn't go anywhere.

### How to Solve:

- Needed to use LLL algorithm.

Okay so here,

```
p = a^51 + 51b^51
p - 51b^51 = a^51
a^51 ≡ p - 51b^51 (mod p)
a^51 ≡ -51b^51 (mod p)
```

Here, I can write:
```
x^51 = -51 (mod p)
```

I don't completely understand this, but it basically helps to reduce the above equation.

```python
start_time = time.time()
xs = Mod(x, n).nth_root(51, all=True)
end_time = time.time()
print(end_time-start_time)
```

It calculates all possible 51st roots of -51 (mod p) using sage. This step essentially looks for integers that satisfy the above equation.

```python
for x in xs:
    L = Matrix([[n, 0], [Integer(x), 1]])
    L = L.LLL()
    a = abs(L[0][0]) 
    b = abs(L[0][1])
```

For each root found, a matrix is created with the first row being [p, 0] and the second row [root, 1]. LLL reduces the matrix to find relations between n and x that lead to possible values of a and b.

### What I learnt:

- Modular Arithmetic Techniques
- Lattice Methods (LLL algo - still need to completely understand, but getting there)