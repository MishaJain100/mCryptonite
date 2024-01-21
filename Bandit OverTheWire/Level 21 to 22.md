<font size = '4'>
<center>
<b>
OverTheWire Bandit - Level 21 to Level 22 Writeup 
</b>
</center>
</font>

<br>
<font size = '3'>

<b>Introduction: </b>
This writeup documents my experience solving Levels 21 to 22 of the OverTheWire Bandit challenge, a CTF-style game focused on learning about security concepts.

<b>Author:</b> Misha Jain

<b>Date:</b> October 26, 2023

<b>Tools Used:</b><br>
Terminal (SSH client)

<b>Challenge Description:</b><br>
Level 21 to Level 22 of Bandit involves connecting to a remote server via SSH and finding a program that runs automatically at regular intervals from cron. We need to examine the configuration to see what command is being executed.

<b>Enumeration:</b><br>
For Level 21, we need to connect to the server using the credentials we obtained in Level 20. Our goal is to identify and examine the cron job to discover the executed command.

<b>Exploitation - Level 21:</b><br>
To connect to the server for Level 21 using SSH, we use the provided credentials:<br>
<center>ssh bandit21@bandit.labs.overthewire.org -p 2220</center><br>
Use the password obtained from Level 20, which is NvEJF7oVjkddltPSrdKEFOllh9V1IBcq to gain access.<br>

<center>

![](<Pictures/Exploitation - Level 21.png>)

</center>

<br>

<b>Password Retrieval - Level 21:</b><br>
The challenge specifies that there is a program running automatically at regular intervals from a cron job, and we need to find the configuration to see what command is being executed.

1. Start by redirecting to the /etc/cron.d directory.
<center>cd /etc/cron.d</center><br>

2. List the contents of the directory. <center>ls</center><br>
You will see a file named "cronjob_bandit22" that is relevant to the task.

3. Examine the contents of the "cronjob_bandit22" file to see the configuration and the executed command. <center>cat cronjob_bandit22</center><br>
The path for a shell code "/usr/bin/cronjob_bandit22.sh" is visible.

4. Display the contents of the shell code. <center>cat /usr/bin/cronjob_bandit22.sh</center><br>
The shell code states the storage of our required password in a file "/tmp/t706lds950RqQh9aMcz6ShpAoZKF7fgv"

5. Display the contents of the file.
<center>cat /tmp/t706lds950RqQh9aMcz6ShpAoZKF7fgv</center><br>

<center>

![](<Pictures/Password Retrieval - Level 21.png>)

</center>

<b>Password – Level 22:</b><br>
The password for Level 22 is: WdDozAdTM2z9DiFEQ2mGlwngMfj4EZff

<b>Exploitation – Level 22:</b><br>
Now that we have the Level 22 password, we can connect to the server for Level 22 using SSH:
<center>ssh bandit22@bandit.labs.overthewire.org -p 2220</center><br>
Use the Level 22 password to gain access.

<center>

![](<Pictures/Exploitation - Level 22.png>)

</center>

<b>Lessons Learned:</b> Level 21 to 22 introduced us to the concept of examining cron job configurations to discover the executed commands. This level reinforced the importance of understanding how cron jobs are used to schedule tasks.

<b>Conclusion:</b><br>
Levels 21 to 22 of the OverTheWire Bandit challenge provided a practical lesson in examining cron job configurations to discover the executed commands. It demonstrated how scheduled tasks can be utilized in security challenges.

</font>