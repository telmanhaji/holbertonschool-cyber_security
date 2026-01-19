# Burp Suite - Fundamentals

Burp Suite is the industry-standard tool for web application security testing. This project covers the fundamental mechanics of using Burp Suite as an intercepting proxy, exploring its core components, and understanding how to leverage it to identify vulnerabilities within the OWASP Top Ten framework.

---

## 📚 Resources

**Read or watch:**

* [Burp Suite Tutorial for Beginners](https://portswigger.net/burp/documentation/desktop/getting-started)
* Getting Started with Burp Suite
* Using Burp to Test for the OWASP Top Ten
* [How to Use Burp Suite - A Beginners Guide](https://www.google.com/search?q=https://www.comparitech.com/net-admin/burp-suite-guide/)
* How to Use Burp Suite to Audit Web Applications

**References:**

* [Official Burp Suite Documentation](https://portswigger.net/burp/documentation)
* [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
* Testing for SQL Injection with Burp Suite
* Burp Suite as a Web Vulnerability Scanner

---

## 🎯 Learning Objectives

By the end of this project, you should be able to explain the following concepts clearly without external help:

### Core Concepts

* **What is Burp Suite?** Understanding its role as a local proxy between the browser and the server.
* **Proxy Setup:** How to configure browser settings and certificates to intercept traffic.
* **HTTPS Configuration:** How to install the Burp CA certificate to intercept encrypted traffic.

### Main Components

* **Spider (Crawler):** How Burp maps out the structure and endpoints of a web application.
* **Repeater:** Its purpose in manually modifying and re-sending individual HTTP requests.
* **Intruder:** How to automate customized attacks (e.g., brute-forcing, fuzzing).
* **Scanner:** Understanding the difference between passive and active scanning and when to trigger them.

### Analysis & Interpretation

* How to interpret Burp Suite results and identify common vulnerabilities like SQLi, XSS, and broken authentication.

---

## ⚙️ Requirements

### General

* **Allowed editors:** `vi`, `vim`, `emacs`.
* **Environment:** All scripts will be tested on **Kali Linux**.
* **Target Environment:** Focus your testing and analysis on the target: `https://web0x02.hbtn.io`.
* **README:** A `README.md` file at the root of the project folder is mandatory.

### Script Constraints

* **Length:** All scripts must be **exactly one line long**.
* **Validation:** `$ wc -l [file]` must return `1`.
* **File Ending:** All files must end with a new line.

---

## 🛠️ Component Overview

| Component | Primary Function |
| --- | --- |
| **Proxy** | Intercepts and modifies traffic between the browser and the server. |
| **Repeater** | Manually tweaks and re-sends individual requests to test server responses. |
| **Intruder** | Automates attacks using payloads to find vulnerabilities or weak credentials. |
| **Scanner** | Automatically crawls and audits the target for security flaws (Pro version). |
| **Decoder** | Transforms encoded data into its canonical form or vice versa (Base64, URL, etc.). |

---

## 📋 Repository Information

* **GitHub repository:** `holbertonschool-cyber_security`
* **Directory:** `web_application_security/0x02_burpsuite_fundamentals`