# Protocols and Servers

In the world of networking, protocols are the "languages" that allow different systems to communicate, share files, and manage infrastructure. This project explores the foundational protocols that power modern networks—from email transmission (SMTP) and file sharing (NFS/SMB) to network monitoring (SNMP) and secure remote access (SSH). Understanding these is critical for both network administration and cybersecurity auditing.

---

## 📚 Resources
* [Network Protocols Explained](https://www.google.com/search?q=https://www.comptia.org/content/guides/network-protocols-explained) (TCP/IP, UDP, ICMP, DNS, DHCP)
* [What is SMTP?](https://www.cloudflare.com/learning/email-security/what-is-smtp/) - Simple Mail Transfer Protocol Explained
* [SNMP Explained](https://www.google.com/search?q=https://www.dnsstuff.com/what-is-snmp): Network Monitoring Protocol Made Easy
* [SMB Protocol Explained](https://www.google.com/search?q=https://www.techtarget.com/searchnetworking/definition/Server-Message-Block-protocol): File Sharing Between Devices
* [Understanding LDAP](https://www.google.com/search?q=https://www.jumpcloud.com/blog/what-is-ldap): Lightweight Directory Access Protocol
* [Remote Desktop Protocol (RDP) Explained](https://www.google.com/search?q=https://www.cloudflare.com/learning/access-management/what-is-rdp/)
* [Cybersecurity Protocols](https://www.google.com/search?q=https://www.fortinet.com/resources/cyberglossary/network-protocols): Understanding HTTPS, SFTP, SSH

**References:**

* [List of Network Protocols and Port Numbers](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml)
* Glossary of Cyber Security Terms
* HackerOne Blog - Network Security Resources

---

## 🎯 Learning Objectives

By the end of this project, you should be able to explain the following concepts clearly without the help of a search engine:

### File Sharing & Management

* **NFS (Network File System):** Its purpose and how it allows remote file access.
* **SMB (Server Message Block):** How it enables file/printer sharing across different operating systems (Windows/Linux).

### Communication & Monitoring

* **SMTP:** The mechanics of how emails are routed and sent across the web.
* **SNMP:** What specific information it provides about the health and status of network devices.

### Identity & Remote Access

* **LDAP:** Its role in centralized authentication and authorization (e.g., Active Directory).
* **RDP:** The inherent security risks of exposing remote desktop ports to the internet.
* **SSH:** Why it is the gold standard for secure, encrypted remote terminal access.

### Network Security Fundamentals

* **Secure vs. Insecure:** Differentiating protocols like **HTTPS/SFTP** from **HTTP/FTP**.
* **Port Numbers:** Their significance in directing traffic to the correct service on a server.
* **Patch Management:** The vital importance of keeping protocol implementations up-to-date to prevent exploitation.

---

## ⚙️ Requirements

### General

* **Operating System:** All files will be run on **Kali Linux 2023.2**.
* **Allowed editors:** `vi`, `vim`, `emacs`.
* **Dynamic Content:** You must substitute the IP range for `$1`.
* **Shebang:** The first line of all your files must be exactly `#!/bin/bash`.

### Constraints

* **Script Length:** All your scripts must be exactly **2 lines long** (`wc -l file` should print 2).
* **Formatting:** All files must end with a new line and be executable.
* **Coding Style:** Your code should follow the **Betty style**. It will be checked using `betty-style.pl` and `betty-doc.pl`.

---

## 🛠️ Protocol Quick-Reference

| Protocol | Port | Description | Security Level |
| --- | --- | --- | --- |
| **SSH** | 22 | Secure Remote Access | High (Encrypted) |
| **SMTP** | 25 | Email Transmission | Low (Unless using STARTTLS) |
| **DNS** | 53 | Domain Name Resolution | Moderate (Unless using DoH) |
| **HTTP** | 80 | Web Traffic | Low (Plaintext) |
| **HTTPS** | 443 | Secure Web Traffic | High (TLS/SSL) |
| **SMB** | 445 | Windows File Sharing | Moderate (Requires signing) |

---

## 📋 Repository Information

* **GitHub repository:** `holbertonschool-cyber_security`
* **Directory:** `linux_security/0x03_protocols_servers`