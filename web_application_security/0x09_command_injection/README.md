***

# Prompt Injections: Command Injection Deep Dive

## 🛡️ Project Overview
This project explores the mechanics of **Command Injection** vulnerabilities, specifically focusing on the theory behind exploits like **CVE-2021-44228** (Log4Shell) and the fundamental Bash scripting concepts required to both execute and prevent these attacks. 

The goal is to understand how untrusted input can be manipulated to execute arbitrary commands on a host operating system.

---

## 🎯 Learning Objectives
By the end of this project, you should be able to explain the following concepts without external assistance:

### Core Concepts
* [ ] **What is Command Injection?** Understanding the vulnerability.
* [ ] **The Mechanics:** How command injection works at the OS level.
* [ ] **Attack Vectors:** Identifying common entry points in web applications.
* [ ] **Impact Assessment:** The potential consequences of a successful system breach.

### Bash & Scripting Mastery
* [ ] **Special Variables:** Understanding Bash special variables and their roles.
* [ ] **Logic Operators:** The difference between `&&` (AND) and `;` (Semicolon) in command execution.
* [ ] **IFS (Internal Field Separator):** What it means and how it dictates word splitting.
* [ ] **Exploitation via IFS:** How to manipulate the separator to bypass filters or change execution flow.

### Defensive & Offensive Tactics
* [ ] **Common Payloads:** Familiarity with standard strings used to test for injection.
* [ ] **Hacker Tricks:** Understanding obfuscation and evasion techniques.
* [ ] **Prevention:** Best practices for securing applications against these vulnerabilities.

---

## 📚 Resources

### Fundamental Reading
| Resource | Description |
| :--- | :--- |
| [Command Injection Overview](https://owasp.org/www-community/attacks/Command_Injection) | OWASP guide on the vulnerability. |
| [BashGuide](https://mywiki.wooledge.org/BashGuide) | Comprehensive guide to mastering Bash. |
| [Bash Special Variables](https://www.gnu.org/software/bash/manual/html_node/Special-Parameters.html) | Documentation on `$?`, `$!`, `$#`, etc. |

### Exploitation & Tools
* **Payloads:** [PayloadsAllTheThings - Command Injection](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Command%20Injection)
* **Networking:** [Interactsh](https://github.com/projectdiscovery/interactsh) (Useful if Burp Suite Pro is unavailable).
* **Techniques:** [HackTricks - Command Injection](https://book.hacktricks.xyz/pentesting-web/command-injection)

---

## 🛠️ Requirements & Environment

### General Specifications
* **Operating System:** All scripts will be tested on **Kali Linux**.
* **Allowed Editors:** `vi`, `vim`, `emacs`.
* **Mandatory File:** A `README.md` file at the root of the project folder.

### Scripting Constraints
* **Length:** All scripts must be **exactly two lines long**. 
  * *Verification:* `wc -l file` should return `2`.
* **Dynamic Input:** Scripts must substitute the target IP range for the first positional parameter (`$1`).
* **Formatting:** All files must end with a new line.

> **Note:** Why end with a new line? It is a POSIX standard that ensures files are processed correctly by various Unix tools and prevents terminal prompts from bleeding into the last line of output.

---

## 🚀 Getting Started

If you are testing for out-of-band interactions and do not have access to Burp Suite Professional, you can use the **Interactsh** docker image:

```bash
# Example for setting up an interactsh client
docker run projectdiscovery/interactsh:latest -v
```

### Script Example Structure
Your scripts should follow this logic:
```bash
#!/bin/bash
[Your Command Logic Here involving $1]
```

---

## ⚖️ Disclaimer
This project is for **educational purposes only**. Unauthorized access to computer systems is illegal. Always practice ethical hacking and obtain permission before testing any environment.
