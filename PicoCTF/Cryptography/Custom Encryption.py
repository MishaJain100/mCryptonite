cipher = [61578, 109472, 437888, 6842, 0, 20526, 129998, 526834, 478940, 287364, 0, 567886, 143682, 34210, 465256, 0, 150524, 588412, 6842, 424204, 164208, 184734, 41052, 41052, 116314, 41052, 177892, 348942, 218944, 335258, 177892, 47894, 82104, 116314]

semi_cipher = []

for i in range (len(cipher)):
    semi_cipher.append(int(cipher[i] / (22 * 311)))

key = 'trudeau'
key_length = 7

flag = ""

for i in range (len(semi_cipher)):
    key_char = key[i % key_length]
    flag += chr(semi_cipher[i] ^ ord(key_char))

print (flag[::-1])