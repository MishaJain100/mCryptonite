<font size = '4'>
<p align = 'center'>
<b>
TetCTF - Stress Release Service Writeup 
</b>
</p>
</font>

<br>
<font size = '3'>

<b>Author:</b> Misha Jain

<b>Date:</b> January 30th, 2023

<b>Challenge Description:</b><br>
For a better New Year, we are introducing a service that can help you reduce stress: http://192.53.173.71:8080 . As our service is only available during the New Year, we are also providing you with a code for later use in material section.

Server: http://192.53.173.71:8080

<br>

<b>Exploitation:</b><br>
Looking at the folder, there were two files, secret.php and index.js. Secret.php was misleading, giving a fake flag. The stress service in index.js lets you shout out your stress, but it has some rules – no letters or numbers, and you can only use a few special characters.

I try using certain Linux commands, but didn't work. Couldn't really figure out how to proceed

</font>