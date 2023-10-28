<font size = '4'>
<center>
<b>
OverTheWire Bandit - Level 12 to Level 13 Writeup 
</b>
</center>
</font>

<br>
<font size = '3'>

<b>Introduction: </b>
This writeup documents my experience solving Levels 12 to 13 of the OverTheWire Bandit challenge, a CTF-style game focused on learning about security concepts.

<b>Author:</b> Misha Jain

<b>Date:</b> October 26, 2023

<b>Tools Used:</b><br>
Terminal (SSH client)

<b>Challenge Description:</b><br>
Level 12 to Level 13 of Bandit involves connecting to a remote server via SSH and finding a password stored in the file "data.txt," which is a hexdump of a compressed file.

<b>Enumeration:</b><br>
For Level 12, we need to connect to the server using the credentials we obtained in Level 11. Our goal is to find a password stored within the "data.txt" file, which is a hexdump of a compressed file.

<b>Exploitation - Level 12:</b><br>
To connect to the server for Level 12 using SSH, we use the provided credentials:<br>
<center>ssh bandit12@bandit.labs.overthewire.org -p 2220</center><br>
Use the password obtained from Level 11, which is JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv to gain access.<br>

<center>

![Alt text](<Pictures/Exploitation - Level 12.png>)

</center>

<br>

<b>Password Retrieval - Level 12:</b><br>
The challenge specifies that the password for Level 13 is stored in the file "data.txt," which is a hexdump of a compressed file. To retrieve the password, we need to reverse the hexdump process. <br>

1. Create a temporary directory to work in. We'll use "/tmp/misha123".
<center>mkdir /tmp/misha123</center><br>

2. Copy the contents of the "data.txt" file to your temporary directory.
<center>cp data.txt /tmp/misha123 </center><br>

3. Change your working directory to the temporary directory.
<center>cd /tmp/misha123</center><br>

4. Display the list of files present in the temporary directory.
<center>ls</center><br>

5. Since data.txt is a hexdump, use the xxd command with the -r tag to revert the hexdump. The '>' operator can be used to store the reverted data in another file, in this case, named "data".
<center>xxd -r data.txt > data</center><br>

6. Display the list of files again. In this case, we can see we have two files, "data" and "data.txt".
<center>ls</center><br>

7. Remove the file "data.txt" as it is no longer necessary.
<center>rm data.txt</center><br>

8. Check the filetype of the new "data" file. This shows its a gzip file.
<center>file data</center><br>

9. Rename the "data" file to have the correct file extension (in this case, ".gz").
<center>mv data data.gz</center><br>

10. Use the gzip -d command to decompress the file.
<center>gzip -d data.gz</center><br>

11. List the files and check the filetype of the new file "data". This shows its a bzip2 file.
<center>ls<br>file data</center><br>

12. Rename the "data" file to have the correct file extension (in this case, ".bz").
<center>mv data data.bz</center><br>

13. Use the bzip2 -d command to decompress the file.
<center>bzip2 -d data.bz</center><br>

14. List the files and check the filetype of the new file "data". This shows its a gzip file.
<center>ls<br>file data</center><br>

15. Rename the "data" file to have the correct file extension (in this case, ".gz").
<center>mv data data.gz</center><br>

16. Use the gzip -d command to decompress the file.
<center>gzip -d data.gz</center><br>

17. List the files and check the filetype of the new file "data". This shows it's a tar file.
<center>ls<br>file data</center><br>

18. Extract the contents of the tar file.<br> <center>tar -xf data</center><br>
-x is an option or flag for the tar command, and it stands for "extract." It tells tar that you want to extract files from an archive.<br>
-f is another option, and it is followed by the name of the archive file you want to work with. In this case, it is "data". The -f option is used to specify the archive file.<br><br>


19. List the files and remove the tar file "data". Then, check the filetype of the new file "data5.bin". This shows it's a tar file.
<center>ls<br>rm data<br>file data5.bin</center><br>

20. Extract the contents of the tar file.
<center>tar -xf data5.bin</center><br>

21. List the files and remove the tar file "data5.bin". Then, check the filetype of the new file "data5.bin". This shows it's a bzip2 file.
<center>ls<br>rm data5.bin<br>file data6.bin</center><br>

22. Rename the "data6.bin" file to have the correct file extension (in this case, ".bz").
<center>mv data6.bin data.bz</center><br>

23. Use the bzip2 -d command to decompress the file.
<center>bzip2 -d data.bz</center><br>

24. List the files and check the filetype of the new file "data". This shows it's a tar file.
<center>ls<br>file data</center><br>

25. Extract the contents of the tar file.
<center>tar -xf data</center><br>

26. List the files and remove the tar file "data". Then, check the filetype of the new file "data8.bin". This shows it's a gzip file.
<center>ls<br>rm data<br>file data8.bin</center><br>

27. Rename the "data8.bin" file to have the correct file extension (in this case, ".gz").
<center>mv data8.bin data.gz</center><br>

28. Use the gzip -d command to decompress the file.
<center>gzip -d data.gz</center><br>

29. List the files and check the filetype of the new file "data". This shows it's an ASCII file.
<center>ls<br>file data</center><br>

30. Display the contents of the ASCII file "data".
<center>cat data</center><br>

<center>

![](<Pictures/Password Retrieval - Level 12_1.png>)
![](<Pictures/Password Retrieval - Level 12_2.png>)

</center>

<b>Password – Level 13:</b><br>
The password for Level 13 is: wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw

<b>Exploitation – Level 13:</b><br>
Now that we have the Level 13 password, we can connect to the server for Level 14 using SSH:
<center>ssh bandit13@bandit.labs.overthewire.org -p 2220</center><br>
Use the Level 13 password to gain access.

<center>

![](<Pictures/Exploitation - Level 13.png>)

</center>

<b>Lessons Learned:</b> Level 12 to 13 introduced us to reversing the process of hexdumping and decompressing files. This level required us to create a temporary directory, copy files, rename files, and use various compression and extraction commands.

<b>Conclusion:</b><br>
Levels 12 to 13 of the OverTheWire Bandit challenge continue to build on shell command knowledge while introducing new challenges involving file compression and extraction. These levels are suitable for beginners to learn more about file manipulation and data decoding.

</font>