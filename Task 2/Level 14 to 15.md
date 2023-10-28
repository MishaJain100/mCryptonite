<font size = '4'>
<center>
<b>
OverTheWire Bandit - Level 14 to Level 15 Writeup 
</b>
</center>
</font>

<br>
<font size = '3'>

<b>Introduction: </b>
This writeup documents my experience solving Levels 14 to 15 of the OverTheWire Bandit challenge, a CTF-style game focused on learning about security concepts.

<b>Author:</b> Misha Jain

<b>Date:</b> October 26, 2023

<b>Tools Used:</b><br>
- Terminal (SSH client)
- Netcat (nc)

<b>Challenge Description:</b><br>
Level 14 to Level 15 of Bandit involves connecting to a remote server via SSH and retrieving the password for the next level by submitting the current level's password to port 30000 on localhost.

<b>Enumeration:</b><br>
For Level 14, we need to connect to the server using the credentials we obtained in Level 13. Our goal is to retrieve the password for Level 15 by submitting the current level's password to a specific port on localhost.

<b>Exploitation - Level 14:</b><br>
To connect to the server for Level 14 using SSH, we use the provided credentials:<br>
<center>ssh bandit14@bandit.labs.overthewire.org -p 2220</center><br>
Use the password obtained from Level 13, which is fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq to gain access.<br>

<center>

![](<Pictures/Exploitation - Level 14.png>)

</center>

<br>

<b>Password Retrieval - Level 14:</b><br>
The challenge specifies that the password for Level 15 can be retrieved by submitting the password of the current level to port 30000 on localhost. To achieve this, you can use the nc (netcat) command.<br>
<center>nc localhost 30000</center><br>

<center>

![](<Pictures/Password Retrieval - Level 14.png>)

</center>

<b>Password – Level 15:</b><br>
The password for Level 15 is: jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt

<b>Exploitation – Level 15:</b><br>
Now that we have the Level 15 password, we can connect to the server for Level 15 using SSH:
<center>ssh bandit15@bandit.labs.overthewire.org -p 2220</center><br>
Use the Level 15 password to gain access.

<center>

![](<Pictures/Exploitation - Level 15.png>)

</center>

<b>Lessons Learned:</b> Level 14 to 15 introduced us to the concept of submitting a password to a specific port on localhost using the nc command. This level reinforced the use of basic network commands for communication with remote services.

<b>Conclusion:</b><br>
Levels 14 to 15 of the OverTheWire Bandit challenge introduced the concept of interacting with a service running on a specific port to retrieve the password for the next level. This level serves as a practical exercise in networking and service interaction.

</font>