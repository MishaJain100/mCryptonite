<font size = '4'>
<center>
<b>
OverTheWire Bandit - Level 15 to Level 16 Writeup 
</b>
</center>
</font>

<br>
<font size = '3'>

<b>Introduction: </b>
This writeup documents my experience solving Levels 15 to 16 of the OverTheWire Bandit challenge, a CTF-style game focused on learning about security concepts.

<b>Author:</b> Misha Jain

<b>Date:</b> October 26, 2023

<b>Tools Used:</b><br>
- Terminal (SSH client)
- Netcat (nc)

<b>Challenge Description:</b><br>
Level 15 to Level 16 of Bandit involves connecting to a remote server via SSH and retrieving the password for the next level by submitting the current level's password to port 30001 on localhost using SSL encryption.

<b>Enumeration:</b><br>
For Level 15, we need to connect to the server using the credentials we obtained in Level 14. Our goal is to retrieve the password for Level 16 by submitting the current level's password to a specific port on localhost using SSL encryption.

<b>Exploitation - Level 15:</b><br>
To connect to the server for Level 15 using SSH, we use the provided credentials:<br>
<center>ssh bandit15@bandit.labs.overthewire.org -p 2220</center><br>
Use the password obtained from Level 14, which is jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt to gain access.<br>

<center>

![](<Pictures/Exploitation - Level 15.png>)

</center>

<br>

<b>Password Retrieval - Level 15:</b><br>
The challenge specifies that the password for Level 16 can be retrieved by submitting the password of the current level to port 30001 on localhost using SSL encryption. To achieve this, you can use the ncat command with the --ssl option.<br>
<center>ncat --ssl localhost 30001</center><br>

<center>

![](<Pictures/Password Retrieval - Level 15.png>)

</center>

<b>Password – Level 16:</b><br>
The password for Level 16 is: JQttfApK4SeyHwDlI9SXGR50qclOAil1

<b>Exploitation – Level 16:</b><br>
Now that we have the Level 16 password, we can connect to the server for Level 16 using SSH:
<center>ssh bandit16@bandit.labs.overthewire.org -p 2220</center><br>
Use the Level 16 password to gain access.

<center>

![](<Pictures/Exploitation - Level 16.png>)

</center>

<b>Lessons Learned:</b> Level 15 to 16 introduced us to the concept of using SSL encryption with the ncat --ssl command to interact with a specific port. This level reinforced the use of network commands for secure communication with remote services.

<b>Conclusion:</b><br>
Levels 15 to 16 of the OverTheWire Bandit challenge introduced the concept of submitting a password to a specific port on localhost using SSL encryption. This level serves as a practical exercise in secure network communication.

</font>