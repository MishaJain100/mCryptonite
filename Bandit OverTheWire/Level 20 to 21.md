<font size = '4'>
<center>
<b>
OverTheWire Bandit - Level 20 to Level 21 Writeup 
</b>
</center>
</font>

<br>
<font size = '3'>

<b>Introduction: </b>
This writeup documents my experience solving Levels 20 to 21 of the OverTheWire Bandit challenge, a CTF-style game focused on learning about security concepts.

<b>Author:</b> Misha Jain

<b>Date:</b> October 26, 2023

<b>Tools Used:</b><br>
- Terminal (SSH client)
- Netcat (nc)

<b>Challenge Description:</b><br>
Level 20 to Level 21 of Bandit involves connecting to a remote server via SSH and using a setuid binary in the home directory to connect to localhost, read a password, and obtain the password for the next level.

<b>Enumeration:</b><br>
For Level 20, we need to connect to the server using the credentials we obtained in Level 19. Our goal is to execute a setuid binary and retrieve the password for Level 21.

<b>Exploitation - Level 20:</b><br>
To connect to the server for Level 20 using SSH, we use the provided credentials:<br>
<center>ssh bandit20@bandit.labs.overthewire.org -p 2220</center><br>
Use the password obtained from Level 19, which is VxCazJaVykI6W36BkBU0mJTCM8rR95XT to gain access.<br>

<center>

![](<Pictures/Exploitation - Level 20.png>)

</center>

<br>

<b>Password Retrieval - Level 20:</b><br>
The challenge specifies that there is a setuid binary in the home directory that connects to localhost on a specified port, reads a line of text, and compares it to the password for the previous level (bandit20). If the password is correct, it will transmit the password for the next level (bandit21).

1. Start by listing the contents of your home directory to find the setuid binary. <center>ls</center><br>
You will see the setuid binary, which is named "suconnect."

2. On another terminal tab, use the nc command to connect to a local port. In this case, we took port 5000. <center>nc -lvp 5000</center><br>
-l tells nc to listen for incoming connections. In other words, it puts nc in "listening" mode.<br>
-v makes nc run in verbose mode, which means it will display more information about the connection as it occurs.<br>

3. In the initial terminal tab, execute suconnect with the port number (5000).
<center>./suconnect 5000</center><br>

4. In the other tab, after the connection has been established, enter the password for Level 20, that is VxCazJaVykI6W36BkBU0mJTCM8rR95XT. The Level 21 password is returned.

<center>

![](<Pictures/Password Retrieval - Level 20_1.png>)
![](<Pictures/Password Retrieval - Level 20_2.png>)

</center>

<b>Password – Level 21:</b><br>
The password for Level 21 is: NvEJF7oVjkddltPSrdKEFOllh9V1IBcq

<b>Exploitation – Level 21:</b><br>
Now that we have the Level 21 password, we can connect to the server for Level 21 using SSH:
<center>ssh bandit21@bandit.labs.overthewire.org -p 2220</center><br>
Use the Level 21 password to gain access.

<center>

![](<Pictures/Exploitation - Level 21.png>)

</center>

<b>Lessons Learned:</b> Level 20 to 21 introduced us to using a setuid binary to communicate with a network daemon and retrieve passwords.
This level reinforced the concept of security implications related to setuid binaries and network communication.

<b>Conclusion:</b><br>
Levels 20 to 21 of the OverTheWire Bandit challenge provided a practical lesson in using a setuid binary to connect to a network daemon, verify passwords, and retrieve the password for the next level.

</font>