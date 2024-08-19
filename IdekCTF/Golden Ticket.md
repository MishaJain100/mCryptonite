# GOLDEN TICKET (Cryptography)

### Challenge Description:

This challenge basically revolved around the concepts of modular arithmetic in cryptography. I'm writing abt this cause a) The other challenges were way too hard to understand, and b) I learnt quite a few interesting concepts while solving this.

### Challenge Code Analysis:

```python
def chocolate_generator(m: int) -> int:
    p = 396430433566694153228963024068183195900644000015629930982017434859080008533624204265038366113052353086248115602503012179807206251960510130759852727353283868788493357310003786807
    return (pow(13, m, p) + pow(37, m, p)) % p
```

This function is where the entirety of the challenge resides. The output given to us is `[chocolate_generator(bytes_to_long(flag)), chocolate_generator(bytes_to_long(flag)) - 1]`. In the above function, p is prime.

### Approach:

Our main approach was the following:
- Make two equations from the given outputs.
- Solve two equations for two variables.

Let,
```
c1 = ((13 ** flag) % p) + ((37 ** flag) % p) % p
c2 = ((13 ** flag-1) % p) + ((37 ** flag-1) % p) % p
```

which can be simplified to
```
c1 = (13.13 ** flag-1 + 37.37 ** flag-1) % p
c2 = (13 ** flag-1 + 37 ** flag-1) % p
```

Replacing `13 ** flag-1 = x` and `37 ** flag-1 = y`, we get
```
c1 = (13x + 37y) % p
c2 = (x + y) % p
```

This is where we got stuck, mostly because we didn't know the laws of modular arithmetics. However, with a little help, we got (eliminating x):
```
24y = (c2 - 13c1) % p
```

Here, we could take inverse mod of 24 on both sides (another thing we didn't know).
Finally, we could solve for y using a discrete log calc.

### Flag:
`idek{charles_and_the_chocolate_factory!!!}`