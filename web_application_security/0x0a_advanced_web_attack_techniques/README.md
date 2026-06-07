# 0x0A. Advanced Web Attack Techniques

## 🛡️ Project Overview
> 💬 *"Security is not a product, but a process."* — Bruce Schneier

Advanced web attacks rarely look dangerous at first glance. A normal-looking request, a slightly unusual log entry, or an unexpected file access pattern can each signal a critical vulnerability hiding in plain sight. Developing the clinical discipline to observe application behavior in real-time and interpret those signals accurately is what separates a thorough penetration tester from a surface-level scanner.

In this project, you will move beyond basic vulnerability identification into active exploitation of advanced web attack techniques. During a realistic testing scenario, you will encounter subtle behavioral signals: anomalous HTTP requests, unexpected server-side file access, and unusual application responses. Each signal is a clue. Your objective is to follow those clues systematically—identifying, analyzing, and exploiting vulnerabilities before a malicious actor does.

---

## 🎯 Learning Objectives
By the end of this project, you are expected to be able to explain the following concepts fluently to anyone, without the help of external search engines:

### Vulnerability Analysis & Exploitation
* [ ] **Risk Assessment:** Evaluate the total business impact and technical risks of advanced web application flaws.
* [ ] **Cross-Site Scripting (XSS):** Identify and classify types of XSS (Stored, Reflected, DOM-based) and understand exactly how they execute in a user's browser context.
* [ ] **Insecure Deserialization:** Understand how untrusted object streams manipulate application logic or trigger Remote Code Execution (RCE).
* [ ] **Server-Side Template Injection (SSTI):** Detect when user input is unsafely rendered inside web template engines (like Jinja2, Twig, or Blade) and upgrade it to host-level access.

### Secure Architecture & Methodology
* [ ] **Behavioral Detection:** Recognize indicators of advanced web vulnerabilities from application logs and raw HTTP traffic patterns.
* [ ] **Defensive Engineering:** Implement proper input validation, context-aware output encoding, and secure coding practices.
* [ ] **SDLC Integration:** Strategically integrate security controls and automated regression checks into the continuous software development lifecycle.

---

## 📚 Resources

### Cross-Site Scripting (XSS)
* [What is Cross-Site Scripting (XSS)?](https://portswigger.net/web-security/cross-site-scripting)
* [How to Prevent XXSS in JavaScript](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
* [Advanced XSS Injection Techniques](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XSS%20Injection)

### Insecure Deserialization
* [Understanding Insecure Deserialization](https://owasp.org/www-project-top-ten/2017/A8_2017-Insecure_Deserialization)
* [Deep Dive: PHP Deserialization Exploits](https://book.hacktricks.xyz/pentesting-web/deserialization)
* [Mitigating Object Injection Vulnerabilities](https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html)

### Server-Side Template Injection (SSTI)
* [SSTI: What it is and How to Prevent It](https://portswigger.net/web-security/server-side-template-injection)
* [SSTI Payload Checklist](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection)

---

## 🛠️ Requirements & Environment

To maintain high technical standards and guarantee proper automated validation, adhere strictly to the following parameters:

### General Specifications
* **Testing Platform:** All tools and exploit scripts will be verified using **Kali Linux**.
* **Allowed Editors:** `vi`, `vim`, or `emacs`.
* **Mandatory File:** A structured `README.md` file must be located at the root directory of the project.

### Technical Guidelines
* ⚠️ **Network Targets:** You must use explicit **IP addresses** directly inside your tasks and scripts. Do **not** pass hostnames.
* 🏁 **File Formatting:** Every file must terminate with a clean trailing newline character.

> **Why the New Line?** In Unix-like ecosystems, a line is structurally defined by its terminating newline character (`\n`). Files missing this boundary break downstream terminal utilities, cause Git to append `\ No newline at end of file` warnings, and interrupt automated grading scripts.

---

## 🌐 Endpoints & Targets

| Task ID | Target Endpoint | Scope Focus |
| :---: | :--- | :--- |
| **Task 0** | `http://web0x0a.task0.hbtn/` | Base Application Audit & Parameter Mapping |
| **Task 1** | `http://web0x0a.task1.hbtn/` | Input Validation & Filter Evasion |
| **Task 2** | `http://web0x0a.task2.hbtn/` | Object Serialization Stream Injections |
| **Task 3** | `http://web0x0a.task3.hbtn/` | Contextual Template Parsing & Expression Injection |
| **Task 4** | `http://web0x0a.task4.hbtn/` | Advanced Chaining & Remote Code Execution (RCE) |

*Note: Base source code for all exercises can be referenced within the tasks' respective working directories.*













