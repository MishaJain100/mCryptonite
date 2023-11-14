<font size = '4'>
<center>
<b>
PicoCTF - buffer overflow 0 Writeup 
</b>
</center>
</font>

<br>
<font size = '3'>

<b>Introduction: </b>
This writeup provides a step-by-step guide for solving the "Buffer Overflow 0" challenge in PicoCTF. The challenge falls under the Binary Exploitation category and requires participants to exploit a buffer overflow vulnerability in a binary executable.

<b>Author:</b> Misha Jain

<b>Date:</b> November 13, 2023

<b>Tools Used:</b><br>
- Terminal
- Text Editor

<b>Challenge Description:</b><br>
The "Buffer Overflow 0" challenge in PicoCTF involves binary exploitation. Participants must analyze the given binary executable to identify and exploit a buffer overflow vulnerability to retrieve the flag.

<b>Exploitation:</b><br>
On opening the source code, we see that on line 40, the gets() function is called, and reads buf1 onto the stack. This function writes the user’s input to the stack without regard to its allocated length. The user can simply overflow this length, and the program will pass their input into the vuln() function to trigger a segmentation fault.

<center>

![](<Pictures/Buffer Overflow 0 - Buffer_Overflow.png>)

</center>

<b>Conclusion:</b><br>
The "Buffer Overflow 0" challenge in PicoCTF provides a practical introduction to buffer overflow exploitation. Participants gain hands-on experience in identifying, analyzing, and exploiting vulnerabilities in binary executables, an essential skill in the field of cybersecurity.

</font>