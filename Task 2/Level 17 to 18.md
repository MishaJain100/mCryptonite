<font size = '4'>
<center>
<b>
OverTheWire Bandit - Level 17 to Level 18 Writeup 
</b>
</center>
</font>

<br>
<font size = '3'>

<b>Introduction: </b>
This writeup documents my experience solving Levels 17 to 18 of the OverTheWire Bandit challenge, a CTF-style game focused on learning about security concepts.

<b>Author:</b> Misha Jain

<b>Date:</b> October 26, 2023

<b>Tools Used:</b><br>
Terminal (SSH client)

<b>Challenge Description:</b><br>
Level 17 to Level 18 of Bandit involves connecting to a remote server via SSH and finding the password for the next level by comparing two files, passwords.old and passwords.new. The password is the only line that has been changed between the two files.

<b>Enumeration:</b><br>
For Level 17, we need to connect to the server using the credentials we obtained in Level 16. Our goal is to find the password for Level 18 by comparing the contents of two files, passwords.old and passwords.new.

<b>Exploitation - Level 17:</b><br>
To connect to the server for Level 17 using SSH, we use the provided credentials:<br>
<center>ssh bandit17@bandit.labs.overthewire.org -p 2220</center><br>
Use the password obtained from Level 16, which is VwOSWtCA7lRKkTfbr2IDh6awj9RNZM5e to gain access.<br>

<center>

![Alt text](<Pictures/Exploitation - Level 17.png>)

</center>

<br>

<b>Password Retrieval - Level 17:</b><br>
The challenge specifies that the password for Level 18 is in passwords.new and is the only line that has been changed between passwords.old and passwords.new. We need to compare these files to find the changed line. We can use the diff command to do so.<br>
<center>diff passwords.old passwords.new</center><br>

<center>

![](<Pictures/Password Retrieval - Level 17.png>)

</center>

<b>Password – Level 18:</b><br>
The password for Level 18 is: hga5tuuCLF6fFzUpnagiMN8ssu9LFrdg

<b>Exploitation – Level 18:</b><br>
Now that we have the Level 18 password, we can connect to the server for Level 18 using SSH:
<center>ssh bandit18@bandit.labs.overthewire.org -p 2220</center><br>
Use the Level 18 password to gain access.

<center>

![](<Pictures/Exploitation - Level 18.png>)

</center>

<b>Lessons Learned:</b> Level 17 to 18 introduced us to the concept of comparing the contents of two files to identify differences. This level reinforced the use of file comparison commands and text analysis.

<b>Conclusion:</b><br>
Levels 17 to 18 of the OverTheWire Bandit challenge provided a simple yet important lesson in file comparison. The challenge requires analyzing and identifying differences between two files to find the changed password.

</font>