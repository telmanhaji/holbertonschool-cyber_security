This is `README.md` for repo about  advanced scanning techniques of Nmap with the strict scripting constraints required for the project.

***

# Nmap Advanced Port Scans

## 🔍 Project Overview
This project focuses on the implementation and analysis of advanced network discovery techniques using **Nmap**. Beyond simple port discovery, we explore how different TCP flag combinations (SYN, ACK, FIN, NULL, Xmas) interact with firewalls and various operating system TCP/IP stacks to reveal open ports, filtering rules, and system vulnerabilities.

---

## 🎯 Learning Objectives
At the completion of this project, you should be able to explain the following concepts fluently without external references:

### Advanced Scanning Mechanics
* [ ] **The "Standard" vs. "Advanced" Difference:** Why basic scans aren't always enough.
* [ ] **TCP Connect vs. SYN Scan:** Understanding the "Half-Open" advantage.
* [ ] **Firewall Probing:** How an **ACK Scan** maps out firewall rulesets.
* [ ] **Stealth & OS Fingerprinting:** Using **FIN, NULL, and Xmas** scans to bypass stateless filters and determine port status.

### Security Strategy
* [ ] **Detection Capabilities:** What information can be exfiltrated through advanced probing?
* [ ] **Defensive Use Cases:** Why Nmap is critical for securing and auditing system ports.
* [ ] **Network Visibility:** Identifying the presence of IDS/IPS or specialized firewall configurations.

---

## 📚 Resources

### Documentation & Guides
| Resource | Link |
| :--- | :--- |
| **Nmap Official Documentation** | [nmap.org/book/man](https://nmap.org/book/man.html) |
| **Advanced Port Scanning Techniques** | [Nmap Chapter 5](https://nmap.org/book/scan-methods.html) |
| **TCP/UDP Port Mapping** | [Nmap Network Scanning](https://nmap.org/book/port-scanning.html) |

### Theoretical References
* **Nmap Advanced Scan Overview:** A deep dive into scan types.
* **Understanding Port Scanners:** How the underlying socket logic works.
* **Firewall Evasion:** Techniques for scanning all 65,535 ports under restriction.

---

## 🛠️ Requirements & Constraints

This project follows strict development standards to ensure script efficiency and compatibility with **Kali Linux**.

### General Environment
* **Platform:** Kali Linux.
* **Editors:** `vi`, `vim`, or `emacs`.
* **Standard:** Scripts must adhere to the **Betty Style** (`betty-style.pl` and `betty-doc.pl`).

### Scripting Rules ("Hard Mode")
To master Bash control flow without shortcuts, the following constraints are active:
* 📏 **Length:** Every script must be **exactly two lines long**.
* 🛑 **Forbidden Syntax:** No backticks, `&&`, `||`, or `;`.
* 🤐 **No `echo`:** Information must be processed/output via the command logic itself.
* 🛡️ **Privilege:** All scripts must start with `sudo`.
* 🏷️ **Variables:** Use `$1` without quotes (e.g., `sudo nmap -sS $1`) to allow for specific shell expansion behaviors.
* 🏁 **Termination:** Files must end with a single new line.

---

## 🚀 Usage

Scripts are designed to take a target IP or range as the first argument.

```bash
# Example: Executing an advanced scan script
./advanced_scan.sh 192.168.1.1
```

### Script Example Structure
```bash
#!/bin/bash
sudo nmap -sX $1
```
*(Note: Use single hyphens `-` for Nmap flags as per project requirements.)*

---

## 📂 Repository Structure

| File | Description |
| :--- | :--- |
| `README.md` | Project documentation and objectives. |
| `[Scripts]` | Two-line executable Bash scripts for specific Nmap techniques. |

---

## ⚖️ Disclaimer
This project is for **educational and ethical security auditing purposes only**. Scanning networks or systems without explicit prior authorization is illegal. Use these tools responsibly to build more resilient infrastructures.

---
*Project by: Telman H. Holberton School Azerbaijan,  Cyber Security*
