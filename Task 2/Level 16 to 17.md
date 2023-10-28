<font size = '4'>
<center>
<b>
OverTheWire Bandit - Level 16 to Level 17 Writeup 
</b>
</center>
</font>

<br>
<font size = '3'>

<b>Introduction: </b>
This writeup documents my experience solving Levels 16 to 17 of the OverTheWire Bandit challenge, a CTF-style game focused on learning about security concepts.

<b>Author:</b> Misha Jain

<b>Date:</b> October 26, 2023

<b>Tools Used:</b><br>
- Terminal (SSH client)
- OpenSSL
- Netcat (nc)

<b>Challenge Description:</b><br>
Level 16 to Level 17 of Bandit involves connecting to a remote server via SSH and retrieving the credentials for the next level by submitting the current level's password to a port on localhost in the range 31000 to 32000. We need to identify which of these ports have a server listening, which of those speak SSL, and which server will provide the next credentials.

<b>Enumeration:</b><br>
For Level 16, we need to connect to the server using the credentials we obtained in Level 15. Our goal is to retrieve the credentials for Level 17 by submitting the current level's password to a specific port on localhost.

<b>Exploitation - Level 16:</b><br>
To connect to the server for Level 16 using SSH, we use the provided credentials:<br>
<center>ssh bandit16@bandit.labs.overthewire.org -p 2220</center><br>
Use the password obtained from Level 15, which is JQttfApK4SeyHwDlI9SXGR50qclOAil1 to gain access.<br>

<center>

![Alt text](<Pictures/Exploitation - Level 16.png>)

</center>

<br>

<b>Password Retrieval - Level 16:</b><br>
The challenge specifies that the credentials for Level 17 can be retrieved by submitting the password of the current level to a port on localhost in the range 31000 to 32000. To achieve this, we need to identify which ports have a server listening, which of those speak SSL, and which server provides the credentials.<br>

1. We'll start by identifying which ports in the specified range (31000 to 32000) have a server actively listening. Use the nmap command to check each port. <center>nmap localhost -p 31000-32000</center>
5 ports, namely 31046, 31518, 31691, 31790 and 31960, are open and actively listening.<br>

2. Next, we need to check which of these servers speak SSL. Use the openssl command with the -s_client option to check each port.<center>openssl s_client -connect localhost:31046 | grep "connected"</center><center>openssl s_client -connect localhost:31518 | grep "connected"</center><center>openssl s_client -connect localhost:31691 | grep "connected"</center><center>openssl s_client -connect localhost:31790 | grep "connected"</center><center>openssl s_client -connect localhost:31960 | grep "connected"</center> <br>
From these, we can see that 31518 and 31790 speak SSL.<br>

3. Using the ncat --ssl command, and entering the password of the current level, we can see which server meets the required credentials. <center>ncat --ssl localhost 31518</center> <center>ncat --ssl localhost 31790</center>
The server 31790 meets the credentials.<br>

4. Copy the RSA private key and use the vim command to store it for further use on your Desktop. Give the private key 400 permissions.
<center>exit</center>
<center>cd Desktop</center>
<center>vim key</center>
<center>chmod 400 key</center><br>

5. Use the ssh -i command to login to the next level using the private key.
<center>ssh -i key bandit17@bandit.labs.overthewire.org -p 2220</center><br>

6. Display the contents of /etc/bandit_pass/bandit17.
<center>cat /etc/bandit_pass/bandit17</center><br>

<center>

![](<Pictures/Password Retrieval - Level 16_1.png>)
![](<Pictures/Password Retrieval - Level 16_2.png>)
![](<Pictures/Password Retrieval - Level 16_3.png>)
![](<Pictures/Password Retrieval - Level 16_4.png>)

</center>

<b>Password – Level 17:</b><br>
The password for Level 17 is: VwOSWtCA7lRKkTfbr2IDh6awj9RNZM5e

<b>Exploitation – Level 17:</b><br>
Now that we have the Level 17 password, we can connect to the server for Level 17 using SSH:
<center>ssh bandit17@bandit.labs.overthewire.org -p 2220</center><br>
Use the Level 17 password to gain access.

<center>

![](<Pictures/Exploitation - Level 17.png>)

</center>

<b>Lessons Learned:</b> Level 16 to 17 introduced us to the concept of identifying open ports and SSL-speaking servers within a specified range. This level required us to understand network communication and SSL encryption.

<b>Conclusion:</b><br>
Levels 16 to 17 of the OverTheWire Bandit challenge introduced the concept of interacting with servers running on specific ports to retrieve the next-level credentials. It served as a practical exercise in network communication and SSL encryption.

</font>