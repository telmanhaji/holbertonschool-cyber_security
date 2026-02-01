# Upload Vulnerabilities

File upload functionality is a common feature in modern web applications, yet it remains one of the most dangerous if not properly secured. This project explores the mechanics of **Unrestricted File Uploads**, how attackers bypass filters to gain **Remote Code Execution (RCE)** via web shells, and the critical defensive layers required to protect a server from malicious uploads.

---

## 📚 Resources

**Read or watch:**

* [File upload vulnerabilities](https://portswigger.net/web-security/file-upload)
* [Unrestricted File Upload](https://owasp.org/www-community/vulnerabilities/Unrestricted_File_Upload)
* [File Upload Attacks Explained](https://www.google.com/search?q=https://www.acunetix.com/blog/articles/file-upload-vulnerabilities/)
* [File Upload Protection – 10 Best Practices](https://www.google.com/search?q=https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Prevention_Cheat_Sheet.html)
* [Preventing File Upload Vulnerabilities](https://www.google.com/search?q=https://www.stackhawk.com/blog/web-file-upload-vulnerabilities-prevention/)
* Testing for Upload Vulnerability
* [Bypass File Upload Restrictions](https://www.google.com/search?q=https://book.hacktricks.xyz/pentesting-web/file-upload)
* Understanding `Content-Type` and `Content-Disposition` Headers

**References:**

* [File Upload Security Checklist](https://www.google.com/search?q=https://github.com/payloadbox/xss-payload-list)
* Understanding MIME Types and File Extensions

---

## 🎯 Learning Objectives

By the end of this project, you should be able to explain the following concepts clearly without the help of a search engine:

* What is an **unrestricted file upload**?
* Why are file uploads a significant security risk?
* How can attackers exploit **file upload forms** to compromise a server?
* What is a **web shell** and how is it used post-exploitation?
* How do **MIME types** relate to upload security?
* What is **Content-Type spoofing**?
* How can **server-side validation** effectively mitigate risks?
* The importance and limitations of **file extension filtering** (Blacklisting vs. Whitelisting).
* How easily **client-side checks** (JavaScript) can be bypassed.
* The best practices for **secure file uploads**.
* How **file size limitations** protect against Denial of Service (DoS).
* The risks associated with **storing uploaded files on the same domain** as the application.
* How **file permissions** (e.g., `chmod`) impact the security of the upload directory.
* Why upload directories should **never be executable**.

---

## ⚙️ Requirements

### General

* **Allowed editors:** `vi`, `vim`, `emacs`.
* **Environment:** All your scripts will be tested on **Kali Linux**.
* **Target:** All tasks focus on the target environment: `Cyber - WebSec 0x05`.
* **README:** A `README.md` file at the root of the folder of the project is mandatory.

### Script Constraints

* **Length:** All your scripts must be **exactly one line long**.
* **Validation:** `$ wc -l file` must print `1`.
* **Formatting:** All your files must end with a new line.

---

## 🛡️ Defensive Overview

| Security Measure | Description |
| --- | --- |
| **Whitelisting** | Only allow specific, safe extensions (e.g., `.jpg`, `.pdf`) instead of blocking dangerous ones. |
| **MIME Validation** | Verify the actual file content, not just the extension provided by the user. |
| **Randomization** | Rename uploaded files to random strings to prevent attackers from easily calling their scripts. |
| **Non-Executable** | Configure the web server (Apache/Nginx) to disable script execution in the upload directory. |

---

## 📋 Repository Information

* **GitHub repository:** `holbertonschool-cyber_security`
* **Directory:** `web_application_security/0x05_upload_vulnerabilities`