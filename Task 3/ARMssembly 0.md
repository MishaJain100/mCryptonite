<font size = '4'>
<center>
<b>
PicoCTF - ARMssembly 0 Writeup 
</b>
</center>
</font>

<br>
<font size = '3'>

<b>Introduction: </b>
This writeup explains the process of solving the "ARMssembly 0" challenge in PicoCTF. The challenge is part of the Reverse Engineering category and requires analyzing an ARM assembly code snippet to find the hidden flag.

<b>Author:</b> Misha Jain

<b>Date:</b> November 11, 2023

<b>Tools Used:</b><br>
- ARM Assembly Knowledge
- Text Editor

<b>Challenge Description:</b><br>
In the "ARMssembly 0" challenge, we are provided with an ARM assembly code snippet. The goal is to understand the assembly code and determine the value that will make the program print the flag.

<b>Exploitation:</b><br>
1. Open the provided ARM Assembly script, "chall.S," using a text editor or IDE, and start reverse engineering from the main function.<br>

<center>

![](<Pictures/ARMssembly 0 - Main_Function.png>)

</center>

2. The initial commands are adjusting the sp (special pointer) value to accomodate the calculations of the register in the stack.<br>

3. The "add x0, x0, 8" command adds 8 bytes to the register x0.

4. The "ldr x0, [x0]" basically loads the value of argument 2 from the stack into string format. x0 points to the first character of the string

<center>

![](<Pictures/ARMssembly 0 - Argument_2.png>)

</center>

5. The "bl atoi" converts Ascii to Integer (atoi). It converts the string value stored in x0 to integer.

<center>

![](<Pictures/ARMssembly 0 - Atoi_Argument_2.png>)

</center>

6. The "mov w19, w0" stores the value of w0 in w19, that is, stores the integer argument 2 in w19.

<center>

![](<Pictures/ARMssembly 0 - w19_Argument_2.png>)

</center>

7. The "add	x0, x0, 16" loads the first argument from the stack, add 16 to it, and loads the value at the resulting address. x0 now points to the first character of the first argument.

<center>

![](<Pictures/ARMssembly 0 - Argument_1.png>)

</center>

8. The string is converted to an integer, then stored in w0. The value of w0 is stored in w1, and the value of w19 is stored in w0.

<center>

![](<Pictures/ARMssembly 0 - Atoi_Argument_1.png>)

</center>

9. The "bl func1" calls function func1.

<center>

![](<Pictures/ARMssembly 0 - Func1.png>)

</center>

10. The "str w0, [sp, 12]" stores the value of w0 onto the stack at an offset of 12 bytes. For simplicity, we can refer to it as sp12. Similarly, the "str w1, [sp, 8]" stores the value of w1 onto the stack at an offset of 8 bytes. We can load the resulting values of sp12 and sp8 into w1 and w0 respectively using the following two commands.

<center>

![](<Pictures/ARMssembly 0 - Swapping_Values.png>)

</center>

11. The following two commands compares the two arguments and calls function .L2 is w1 is less than or equal to w2. This condition is false, so it will skip over that command.

<center>

![](<Pictures/ARMssembly 0 - Comparison.png>)

</center>

12. The "ldr w0, [sp, 12]" stores the value of sp12 in w0.

<center>

![](<Pictures/ARMssembly 0 - Func1_Storage_Final.png>)

</center>

13. The following commands just print the result, that is argument 2, followed by register clean-up.

<center>

![](<Pictures/ARMssembly 0 - Result.png>)

</center>

14. The flag is the result in hexadecimal form, hence the flag is "picoCTF{6D1D2DD1}".<br><br>

<b>Conclusion:</b><br>
The "ARMssembly 0" challenge in PicoCTF introduces us to ARM assembly language and basic reverse engineering. By analyzing the assembly code, we can identify the conditions for printing the flag and determine the correct input.

</font>