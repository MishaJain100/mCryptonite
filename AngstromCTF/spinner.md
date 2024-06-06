<font size = '4'>
<p align = 'center'>
<b>
AngstromCTF - spinner Writeup 
</b>
</p>
</font>

<br>
<font size = '3'>

<b>Challenge Description:</b><br>

spin 10,000 times for flag

https://spinner.web.actf.co

<br>

<b>Exploitation:</b><br>

Looking at the code, we see a function defined:

```js
const message = async () => {
    if (state.flagged) return
    const element = document.querySelector('.message')
    element.textContent = Math.floor(state.total / 360)

    if (state.total >= 10_000 * 360) {
        state.flagged = true
        const response = await fetch('/falg', { method: 'POST' })
        element.textContent = await response.text()
    }
}
message()
```

To get the flag, the following commands are inputted in the console:
```js
state.total = 10000 * 360;
> 3600000
state.flagged = false
> false
message();
> Promise {<pending>}
```

The flag is printed.

Flag: `actf{b152d497db04fcb1fdf6f3bb64522d5e}`