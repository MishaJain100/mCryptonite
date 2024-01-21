<font size = '4'>
<p align = 'center'>
<b>
KnightCTF - Gain Access 1 Writeup 
</b>
</p>
</font>

<br>
<font size = '3'>

<b>Author:</b> Misha Jain

<b>Date:</b> January 21st, 2023

<b>Challenge Description:</b><br>
The web challenges are very much similar to real life application bugs. This is going to be a series of Gain Access with 3 challenges unlocks upon solving one by one. By solving these challenges, you'll gain a practical knowledge of Authentication Bypass Vulnerabilites as well as business logic error. The only difference is you'll not get any bounty but you'll get flags. Give it a try. And keep in mind, Don't make it hard, keep it simple. All the best. Solve the challenges & be a cyber knight.

No need to bruteforce. There's a rate limit. If you send continuous requests, you'll be blocked for 3 minutes.

Target : http://45.33.123.243:13556/

<br>

<b>Exploitation:</b><br>
Following the link address, I was directed to a login page. The required email address was given in a comment when you inspected the source of the page.

<p align = 'center'>

![](<Pictures/Gain Access 1 - Email.png>)

</p><br>

Clicking the reset password button, and entering the email address 'root@knightctf.com', it said that the password reset token was sent to the email.

(Don't know how to access the password token)

</font>