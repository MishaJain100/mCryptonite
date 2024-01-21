<font size = '4'>
<p align = 'center'>
<b>
KnightCTF - Kitty Writeup 
</b>
</p>
</font>

<br>
<font size = '3'>

<b>Author:</b> Misha Jain

<b>Date:</b> January 21st, 2023

<b>Challenge Description:</b><br>
Tetanus is a serious, potentially life-threatening infection that can be transmitted by an animal bite.

N:B: There is no need to do bruteforce.

Target : http://45.33.123.243:5020/

<br>

<b>Exploitation:</b><br>
Following the link address, I was directed to a login page. Upon viewing the source of the page, I saw a CSS file and a JS file. The CSS file did not give any significant information. The JS file gave me the username and password required for login.

<p align = 'center'>

![](<Pictures/Kitty - Page_Source.png>)

</p><br>

<p align = 'center'>

![](<Pictures/Kitty - JS.png>)

</p><br>

Entering the username and password, I came across another webpage, with some posts. Viewing the source for this webpage, the script showed that we could enter cat flag.txt as an input. This displayed the flag.

<p align = 'center'>

![](<Pictures/Kitty - Final_Script.png>)

</p><br>

<p align = 'center'>

![](<Pictures/Kitty - Flag.png>)

</p><br>

<b>Flag:</b> KCTF{Fram3S_n3vE9_L1e_4_toGEtH3R}

</font>