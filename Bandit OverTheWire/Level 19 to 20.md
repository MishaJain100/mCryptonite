<font size = '4'>
<center>
<b>
OverTheWire Bandit - Level 19 to Level 20 Writeup 
</b>
</center>
</font>

<br>
<font size = '3'>

<b>Introduction: </b>
This writeup documents my experience solving Levels 19 to 20 of the OverTheWire Bandit challenge, a CTF-style game focused on learning about security concepts.

<b>Author:</b> Misha Jain

<b>Date:</b> October 26, 2023

<b>Tools Used:</b><br>
Terminal (SSH client)

<b>Challenge Description:</b><br>
Level 19 to Level 20 of Bandit involves connecting to a remote server via SSH and using a setuid binary in the home directory to gain access to the password for the next level.

<b>Enumeration:</b><br>
For Level 19, we need to connect to the server using the credentials we obtained in Level 18. Our goal is to execute a setuid binary and retrieve the password for Level 20.

<b>Exploitation - Level 19:</b><br>
To connect to the server for Level 19 using SSH, we use the provided credentials:<br>
<center>ssh bandit19@bandit.labs.overthewire.org -p 2220</center><br>
Use the password obtained from Level 18, which is awhqfNnAbc1naukrpqDYcF95h7HoMTrC to gain access.<br>

<center>

![](<Pictures/Exploitation - Level 19.png>)

</center>

<br>

<b>Password Retrieval - Level 19:</b><br>
The challenge specifies that to access the password for Level 20, we should use a setuid binary in the home directory. We need to execute this binary without any arguments to find out how to use it. First, lets use the ls command to list the files available. <center>ls -l</center><br>
We see that we have a setuid binary file called bandit20-do. Let's execute it. <center>./bandit20-do</center><br>
A setuid binary file allows one to execute commands with elevated priviledges. In this case, we get the priviledges of the user "bandit20".<br>
Use the cat command as bandit20 to display the password stored in the /etc/bandit_pass file.
<center>./bandit20-do cat /etc/bandit_pass/bandit20</center><br>

<center>

![](<Pictures/Password Retrieval - Level 19.png>)

</center>

<b>Password – Level 20:</b><br>
The password for Level 20 is: VxCazJaVykI6W36BkBU0mJTCM8rR95XT

<b>Exploitation – Level 20:</b><br>
Now that we have the Level 20 password, we can connect to the server for Level 20 using SSH:
<center>ssh bandit20@bandit.labs.overthewire.org -p 2220</center><br>
Use the Level 20 password to gain access.

<center>

![](<Pictures/Exploitation - Level 20.png>)

</center>

<b>Lessons Learned:</b> Level 19 to 20 introduced us to the use of setuid binaries to execute commands with elevated privileges. This level reinforced the importance of understanding how setuid binaries work and their security implications.

<b>Conclusion:</b><br>
Levels 19 to 20 of the OverTheWire Bandit challenge provided a practical lesson in using setuid binaries to execute commands with elevated privileges. By following the provided instructions, we were able to access the password for Level 20.

</font>