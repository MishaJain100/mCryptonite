# PUMP IT UP (Cryptography)

### Challenge Description:

Don't you know? Pump It Up!

### Given: 

Two python scripts:
- pump.py: Takes flag, converts to sound snippets using hex chars, and encrypts the combined sound data file.

```python
def encrypt_it():
    key = secrets.token_bytes(16)
    cipher = AES.new(key, AES.MODE_ECB)
    with open("flag.voc", "rb") as f:
        val = f.read()
    val += b"\x00" * (16 - len(val) % 16)
    with open("flag.enc", "wb") as f:
        f.write(cipher.encrypt(val))
```

This encrypts flag.voc with AES in ECB mode.

- audio_engine.py: Handles the reading and writing of `.voc` files.

```python
def extract_sound_data(voc_filename):
    with open(voc_filename, 'rb') as voc_file:
        voc_file.read(26)
        return voc_file.read()[:-1]
```

This function reads the sound data from each .voc snippet, and skips the header bytes.

```python
def create_voc_file(output_filename, sound_data_blocks):
    with open(output_filename, 'wb') as output_file:
        output_file.write(b'Creative Voice File\x1A\x1A\x00\x14\x01\x1f\x11')
        output_file.write(sound_data_blocks + b"\x00")
```

This creates a .voc file by combining multiple sound data blocks into one file.

### Approach used:

What is AES with ECB?

AES encryption in ECB takes the data and splits it into fixed 16 byte chunks, and it doesn't randomize identical blocks. This can help in pattern recognition, which is basically what the solve script has done.
Each hex character in the flag corresponds to a unique .voc sound snippet, so the encrypted flag.enc can be treated as a substitution cipher with each 16 byte chunk representing a hex digit.

### How to Solve:

```python
import string
from collections import OrderedDict

OFFSET_ONE = 0x2eec0
OFFSET_TWO = 0x2eed0
datasets = []

with open("../PUBLIC/flag.enc", "rb") as fp:
    fp.read(16*2)  # Skipping first 32 bytes
    last_one = False
    while True:
        data = fp.read(16)
        if not data:
            break
        datasets.append(data)
        print(data.hex())
        fp.read(OFFSET_ONE if last_one else OFFSET_TWO)
        last_one = not last_one
```

Reading flag.enc in 16-byte chunks.

```python
out = []
uniq = list(OrderedDict.fromkeys(datasets))
placeholders = string.ascii_uppercase[6:]
for cnt, itm in enumerate(datasets):
    out.append(placeholders[uniq.index(itm)])
print("".join(out))
```

This is just creating a sequence of placeholders to represent the flag.

```python
known_start = b"flag{y0u_".hex()
known_end = b"}".hex()          

mappings = {k: b"" for k in list(set(out))}
for ind, s in enumerate(known_start):
    mappings[out[ind]] = s 

if mappings[out[-1]] == b"":
    mappings[out[-1]] = known_end[1]
if mappings[out[-2]] == b"":    
    mappings[out[-2]] = known_end[0]

```

We know the flag starts with `flag{y0u_` and ends with `}`. Using that, we can map placeholders to their hex values.

```python
new_attmpt = "".join(out)
for k, v in mappings.items():
    if v != b"":
        new_attmpt = new_attmpt.replace(k, v)

debugge = new_attmpt
printable = ""
for c in range(0, len(debugge), 2):
    if all([x in string.hexdigits for x in debugge[c:c+2]]):
        printable += chr(int(debugge[c:c+2], 16))
    else:
        printable += "?"

print("Flag:", printable)
```

This just replaces the placeholders in out with the hex values in mappings, then converting hex to ASCII.

### Things Learnt:

- ECB mode is breakable by pattern recognition.