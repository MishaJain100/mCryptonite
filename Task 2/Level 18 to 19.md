<font size = '4'>
<center>
<b>
OverTheWire Bandit - Level 18 to Level 19 Writeup 
</b>
</center>
</font>

<br>
<font size = '3'>

<b>Introduction: </b>
This writeup documents my experience solving Levels 18 to 19 of the OverTheWire Bandit challenge, a CTF-style game focused on learning about security concepts.

<b>Author:</b> Misha Jain

<b>Date:</b> October 26, 2023

<b>Tools Used:</b><br>
Terminal (SSH client)

<b>Challenge Description:</b><br>
Level 18 to Level 19 of Bandit involves connecting to a remote server via SSH and finding the password for the next level stored in a file named "readme" in the home directory. However, the .bashrc file has been modified to log you out when you log in with SSH.

<b>Enumeration:</b><br>
For Level 18, we need to connect to the server using the credentials we obtained in Level 17. Our goal is to retrieve the password for Level 19 from the "readme" file.

<b>Exploitation - Level 18:</b><br>
To connect to the server for Level 18 using SSH, we use the provided credentials:<br>
<center>ssh bandit18@bandit.labs.overthewire.org -p 2220</center><br>
Use the password obtained from Level 17, which is hga5tuuCLF6fFzUpnagiMN8ssu9LFrdg to gain access.<br>

<center>

![Alt text](<Pictures/Exploitation - Level 18.png>)

</center>

<br>

<b>Password Retrieval - Level 18:</b><br>
The challenge specifies that the password for Level 19 is stored in a file named "readme" in the home directory. However, there is a modification to the .bashrc file that logs you out upon SSH login. To overcome this, we can use the -t (pseudo-terminal) option to run a specific command. In this case, we'll use cat to read the contents of the "readme" file:
<center>ssh -t bandit18@bandit.labs.overthewire.org -p 2220 "cat readme"</center><br>

<center>

![](<Pictures/Password Retrieval - Level 18.png>)

</center>

<b>Password – Level 19:</b><br>
The password for Level 19 is: awhqfNnAbc1naukrpqDYcF95h7HoMTrC

<b>Exploitation – Level 19:</b><br>
Now that we have the Level 19 password, we can connect to the server for Level 19 using SSH:
<center>ssh bandit19@bandit.labs.overthewire.org -p 2220</center><br>
Use the Level 19 password to gain access.

<center>

![](<Pictures/Exploitation - Level 19.png>)

</center>

<b>Lessons Learned:</b> Level 18 to 19 introduced us to using the -t option to run a specific command upon SSH login to overcome modifications to the .bashrc file. This level reinforced the use of SSH command options and dealing with login scripts.

<b>Conclusion:</b><br>
Levels 18 to 19 of the OverTheWire Bandit challenge demonstrate the importance of understanding how login scripts can impact the SSH login process. By using the -t option to run a specific command, we were able to bypass the modified .bashrc file and retrieve the password.

</font>