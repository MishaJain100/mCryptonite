<font size = '4'>
<p align = 'center'>
<b>
DiceCTF - dicedicegoose Writeup 
</b>
</p>
</font>

<br>
<font size = '3'>

<b>Author:</b> Misha Jain

<b>Date:</b> February 10th, 2023

<b>Challenge Description:</b><br>
Follow the leader.

ddg.mc.ax

<br>

<b>Exploitation:</b><br>
Opening the URL revealed a game, where the objective seemed to be to overlap the goose with our player, the dice.

<p align = 'center'>

![](<Pictures/Dicedicegoose - Game.png>)

</p><br>

I viewed the source code, and searched for a flag statement. The statement stated that if our score equalled 9, then it would reveal the flag with encoded history.

<p align = 'center'>

![](<Pictures/Dicedicegoose - Flag_Code.png>)

</p><br>

History is an array containing the player moves, followed by the goose moves. The goose moves are random. To get a length of 9, I sent the following commands to console:

<p align = 'center'>

![](<Pictures/Dicedicegoose - Flag.png>)

</p><br>

<b>Flag:</b> dice{pr0_duck_gam3r_AAEJCQEBCQgCAQkHAwEJBgQBCQUFAQkEBgEJAwcBCQIIAQkB}

</font>