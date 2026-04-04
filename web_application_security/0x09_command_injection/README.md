# 🛡️ Command Injection (CVE‑2021‑44228 Explained)
### Holberton School Azerbaijan — Cybersecurity Project    
**Date:** April 2026  

---

## 📌 Overview

This project dives deep into **Command Injection vulnerabilities**, one of the most dangerous and common security flaws found in insecure web applications. You will explore how these attacks work, learn to identify them, understand the underlying Bash mechanisms that make them possible, and review methods to prevent them.

This repository is part of the **Holberton School Azerbaijan** project-based curriculum, focusing on real-world, hands-on cybersecurity learning.

---

## 🎯 Learning Objectives

By the end of this project, you should be able to clearly explain:

### ✅ Core Concepts
- What **command injection** is  
- How command injection works internally  
- Common payload patterns (high‑level understanding only)  
- Typical attack vectors used by attackers  

### ✅ Bash Knowledge
- Bash special variables  
- The difference between:
  - `&&` (conditional execution)
  - `;` (sequential execution)
- What **IFS (Internal Field Separator)** is  
- How manipulating **IFS** affects command execution  

### ✅ Offensive Security Awareness
- Common techniques used by attackers  
- How DNS or callback tools (like **interactsh**) are used to detect exploitability  

### ✅ Defensive Security
- Practical steps to defend web applications  
- Secure coding principles  
- Proper input validation strategies  

---

## 🧠 What Is Command Injection?

**Command Injection** happens when a web application passes **untrusted user input** directly into a system command.  
This allows an attacker to **inject additional commands** that the server executes.

It can lead to:
- Full system compromise  
- Data exfiltration  
- Privilege escalation  
- Remote Code Execution (RCE)  

---

## 🏗️ Project Requirements

✅ All Bash scripts must:  
- Be written using `vi`, `vim`, or `emacs`  
- Contain **exactly two lines**  
- Accept an argument representing an IP range → `$1`  
- Be tested on **Kali Linux**  
- End with a newline  
- Follow proper shell formatting standards  

✅ `README.md` is mandatory (this file)

---

## 📦 Tools & Resources

You should review these as part of your research:

- Command Injection Overview  
- BashGuide  
- Payload Lists (conceptually)  
- Bash Special Variables documentation  
- Bash operators (`&&`, `;`)  
- Internal Field Separator (IFS)  
- interactsh (for receiving callbacks if you do not have Burp Suite Pro)

---

## 🧩 Example Topics You Will Understand

### 🔹 Why does this work?

```bash
ping $USER_INPUT
