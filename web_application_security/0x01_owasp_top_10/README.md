# OWASP Top 10

This project is a deep dive into the **OWASP Top 10**, the standard awareness document for developers and web application security. It represents a broad consensus on the most critical security risks to web applications. Understanding these vulnerabilities is fundamental for any cybersecurity professional or web developer aiming to build secure, resilient systems.

---

## 📚 Resources

**Read or watch:**

* [OWASP Top 10:2021](https://owasp.org/www-project-top-ten/)
* [Explaining the OWASP Top 10](https://www.cloudflare.com/learning/security/threats/owasp-top-10/)
* Understanding the OWASP Top 10 with Examples
* OWASP Top 10: The Big Picture
* OWASP Top 10 Risks – Mitigation Strategies
* [How to Choose a Password](https://www.google.com/search?q=https://www.nist.gov/featured-stories/back-basics-creating-strong-passwords)

**References:**

* [OWASP Official Website](https://owasp.org/)
* [OWASP Top 10 - Wikipedia](https://en.wikipedia.org/wiki/OWASP)
* [OWASP Top 10 Proactive Controls](https://owasp.org/www-project-proactive-controls/)
* [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)
* [OWASP ZAP](https://www.zaproxy.org/) - Web Application Penetration Testing Tool
* [OWASP Amass](https://github.com/owasp-amass/amass) - Subdomain Enumeration Tool
* [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/) - Vulnerable Web Application
* [OWASP Dependency-Check](https://owasp.org/www-project-dependency-check/) - Software Composition Analysis Tool

---

## 🎯 Learning Objectives

At the end of this project, you are expected to be able to explain the following to anyone, **without the help of Google**:

* What exactly is the **OWASP Top 10**?
* Why is **Injection** (SQL, NoSQL, OS) so dangerous?
* How does **Cross-Site Scripting (XSS)** affect web applications and users?
* What is the risk associated with **Broken Authentication**?
* Can you explain **Sensitive Data Exposure** (Cryptographic Failures)?
* Describe a **Security Misconfiguration** and its consequences.
* What is **XML External Entity (XXE)**?
* How do **Broken Access Controls** impact overall system security?
* What are the most common web application security flaws?
* How to prevent **Insecure Deserialization**?
* What is the critical use of **Security Logging and Monitoring**?
* Explain the risks of using **components with known vulnerabilities**.
* How can using **APIs** increase modern security risks?

---

## ⚙️ Requirements

### General

* **Operating System:** All files will be run on **Kali Linux 2023.2**.
* **Allowed editors:** `vi`, `vim`, `emacs`.
* **Dynamic Content:** You must substitute the IP range for `$1`.
* **Shebang:** The first line of all your files must be exactly `#!/bin/bash`.
* **Script Constraints:**
* You are **not allowed** to use backticks, `&&`, `||`, or `;`.
* All your files must end with a new line.


* **Coding Style:** Your code should follow the **Betty style**. It will be checked using `betty-style.pl` and `betty-doc.pl`.

---

## 🛠️ Key Vulnerability Overview

| Category | Vulnerability | Description |
| --- | --- | --- |
| **A01:2021** | **Broken Access Control** | Restrictions on what authenticated users are allowed to do are not properly enforced. |
| **A03:2021** | **Injection** | User-supplied data is not validated, filtered, or sanitized by the application. |
| **A07:2021** | **Identification and Authentication Failures** | Problems with session management and user identity confirmation. |
| **A08:2021** | **Software and Data Integrity Failures** | Code and infrastructure that does not protect against integrity violations. |

---

## 📋 Repository Information

* **GitHub repository:** `holbertonschool-cyber_security`
* **Directory:** `web_application_security/0x0c_owasp_top_10`