<font size = '4'>
<center>
<b>
OverTheWire Bandit - Level 13 to Level 14 Writeup 
</b>
</center>
</font>

<br>
<font size = '3'>

<b>Introduction: </b>
This writeup documents my experience solving Levels 13 to 14 of the OverTheWire Bandit challenge, a CTF-style game focused on learning about security concepts.

<b>Author:</b> Misha Jain

<b>Date:</b> October 26, 2023

<b>Tools Used:</b><br>
Terminal (SSH client)

<b>Challenge Description:</b><br>
Level 13 to Level 14 of Bandit involves connecting to a remote server via SSH and retrieving a private SSH key that can be used to log into the next level. The password for the next level is stored in /etc/bandit_pass/bandit14 and can only be read by user "bandit14."

<b>Enumeration:</b><br>
For Level 13, we need to connect to the server using the credentials we obtained in Level 12. Our goal is to retrieve the private SSH key that will allow us to access the next level.

<b>Exploitation - Level 13:</b><br>
To connect to the server for Level 13 using SSH, we use the provided credentials:<br>
<center>ssh bandit13@bandit.labs.overthewire.org -p 2220</center><br>
Use the password obtained from Level 12, which is wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw to gain access.<br>

<center>

![Alt text](<Pictures/Exploitation - Level 13.png>)

</center>

<br>

<b>Password Retrieval - Level 13:</b><br>
The challenge specifies that the password for Level 14 is stored in /etc/bandit_pass/bandit14 and can only be read by user "bandit14." To retrieve this password, we need to obtain the private SSH key that will allow us to log in as "bandit14."<br>

1. Use the ssh -i command to login to the next level using the private key.
<center>ssh -i sshkey.private bandit14@bandit.labs.org</center><br>

2. Display the contents of /etc/bandit_pass/bandit14.
<center>cat /etc/bandit_pass/bandit14</center><br>

<center>

![](<Pictures/Password Retrieval - Level 13_1.png>)
![](<Pictures/Password Retrieval - Level 13_2.png>)

</center>

<b>Password – Level 14:</b><br>
The password for Level 14 is: fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq

<b>Exploitation – Level 14:</b><br>
Now that we have the Level 14 password, we can connect to the server for Level 14 using SSH:
<center>ssh bandit14@bandit.labs.overthewire.org -p 2220</center><br>
Use the Level 14 password to gain access.

<center>

![Alt text](<Pictures/Exploitation - Level 14.png>)

</center>

<b>Lessons Learned:</b> Level 13 to 14 introduced us to the concept of using a private SSH key to access a higher-level account. This level required us to understand SSH key authentication and file permissions.

<b>Conclusion:</b><br>
Levels 13 to 14 of the OverTheWire Bandit challenge introduced the use of a private SSH key to access a higher-level account and retrieve the password for the next level. This level serves as a practical exercise in SSH key authentication.

</font>