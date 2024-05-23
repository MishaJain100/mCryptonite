import string

ALPHABET = string.ascii_lowercase[:16]

def b16_decode(enc):
    dec = ""
    for i in range (0, len(enc), 2):
        binary = "{0:04b}".format(ALPHABET.index(enc[i])) + "{0:04b}".format(ALPHABET.index(enc[i + 1]))
        dec += chr(int(binary, 2))
    return dec

def shift(c, k): #h, k
	t1 = ord(c) - ord('a')
	t2 = ord(k) - ord('a')
	return ALPHABET[(t1 - t2) % len(ALPHABET)]

enc = 'mlnklfnknljflfmhjimkmhjhmljhjomhmmjkjpmmjmjkjpjojgjmjpjojojnjojmmkmlmijimhjmmj'

for key in ALPHABET:
    flag = ""
    for i in enc:
        flag += shift(i, key) #hc
    print (b16_decode(flag))
