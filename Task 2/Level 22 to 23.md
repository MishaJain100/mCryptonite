<font size = '4'>
<center>
<b>
OverTheWire Bandit - Level 22 to Level 23 Writeup 
</b>
</center>
</font>

<br>
<font size = '3'>

<b>Introduction: </b>
This writeup documents my experience solving Levels 22 to 23 of the OverTheWire Bandit challenge, a CTF-style game focused on learning about security concepts.

<b>Author:</b> Misha Jain

<b>Date:</b> October 26, 2023

<b>Tools Used:</b><br>
Terminal (SSH client)

<b>Challenge Description:</b><br>
Level 22 to Level 23 of Bandit involves connecting to a remote server via SSH and finding a program that runs automatically at regular intervals from cron. We need to examine the configuration to see what command is being executed.

<b>Enumeration:</b><br>
For Level 22, we need to connect to the server using the credentials we obtained in Level 21. Our goal is to identify and examine the cron job to discover the executed command.

<b>Exploitation - Level 22:</b><br>
To connect to the server for Level 22 using SSH, we use the provided credentials:<br>
<center>ssh bandit22@bandit.labs.overthewire.org -p 2220</center><br>
Use the password obtained from Level 21, which is WdDozAdTM2z9DiFEQ2mGlwngMfj4EZff to gain access.<br>

<center>

![](<Pictures/Exploitation - Level 22.png>)

</center>

<br>

<b>Password Retrieval - Level 22:</b><br>
The challenge specifies that there is a program running automatically at regular intervals from a cron job, and we need to find the configuration to see what command is being executed.

1. Start by redirecting to the /etc/cron.d directory.
<center>cd /etc/cron.d</center><br>

2. List the contents of the directory. <center>ls</center><br>
You will see a file named "cronjob_bandit23" that is relevant to the task.

3. Examine the contents of the "cronjob_bandit23" file to see the configuration and the executed command. <center>cat cronjob_bandit22</center><br>
The path for a shell code "/usr/bin/cronjob_bandit23.sh" is visible.

4. Display the contents of the shell code. <center>cat /usr/bin/cronjob_bandit22.sh</center><br>
The shell code states the storage of our required password in a file "/tmp/$mytarget", where mytarger is a variable equating to the evaluation of the command "echo I am user $myname | md5sum | cut -d ' ' -f 1".<br>myname is another variable which is equating to "bandit23"

5. Run the command in the terminal. <center>echo I am user $myname | md5sum | cut -d ' ' -f 1</center><br>
This returns a value "8ca319486bfbbc3663ea0fbe81326349".


5. Display the contents of the file.
<center>cat /tmp/8ca319486bfbbc3663ea0fbe81326349</center><br>

<center>

![](<Pictures/Password Retrieval - Level 22.png>)

</center>

<b>Password – Level 23:</b><br>
The password for Level 23 is: QYw0Y2aiA672PsMmh9puTQuhoz8SyR2G

<b>Exploitation – Level 23:</b><br>
Now that we have the Level 23 password, we can connect to the server for Level 23 using SSH:
<center>ssh bandit23@bandit.labs.overthewire.org -p 2220</center><br>
Use the Level 23 password to gain access.

<center>

![](<Pictures/Exploitation - Level 23.png>)

</center>

<b>Lessons Learned:</b> Level 22 to 23 introduced us to the concept of examining cron job configurations to discover the executed commands. This level reinforced the importance of understanding how cron jobs work and how to read and execute shell scripts written by others.

<b>Conclusion:</b><br>
Levels 22 to 23 of the OverTheWire Bandit challenge provided a practical lesson in examining cron job configurations to discover the executed commands and executing shell scripts to understand their functionality.

</font>