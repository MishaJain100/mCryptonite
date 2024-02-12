<font size = '4'>
<p align = 'center'>
<b>
DiceCTF - funnylogin Writeup 
</b>
</p>
</font>

<br>
<font size = '3'>

<b>Author:</b> Misha Jain

<b>Date:</b> February 10th, 2023

<b>Challenge Description:</b><br>
can you login as admin?

NOTE: no bruteforcing is required for this challenge! please do not bruteforce the challenge.

funnylogin.mc.ax

<br>

<b>Exploitation:</b><br>
The URL led to a login page. Downloading the .gz file, and looking into it, I saw an app.js file. Looking at the code, I could see that it generated 100,000 users at random, and then chose a random user and set it as the admin.

<p align = 'center'>

![](<Pictures/Funnylogin - Code.png>)

</p><br>

Problem is, we don't know which user is the admin. A dictionary called isAdmin is used to set a user as the newAdmin by setting its value to true.

Every object in Javascript has a method called proto, which is always set to true. This method can be used by other objects to inherit properties of the parent object.

I entered username as __proto__, and a simple sqli in the password [1' or 1=1--]. However, I got a pop-up.

<p align = 'center'>

![](<Pictures/Funnylogin - Popup.png>)

</p><br>

I looked at the javascript code again, and saw that if id == 0, it will fail the if condition. Hence I edited the sqli to be `1' or 1=1 and id > 1--`.

<p align = 'center'>

![](<Pictures/Funnylogin - Code_If_Else.png>)

</p><br>

<b>Flag:</b> dice{i_l0ve_java5cript!}

</font>