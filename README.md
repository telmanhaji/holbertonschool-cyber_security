# 🛡️ Introduction to Cyber Security

Welcome to the **Introduction to Cyber Security** project. This repository serves as a foundational guide into the world of information security, ethical hacking, and the tools used to protect digital assets. Through theoretical concepts and practical application using **Kali Linux**, you will explore how to secure systems, understand threats, and manage risks.



## 📋 Concepts

This project covers the following core areas:
* **Cyber Security Fundamentals:** The practice of protecting systems, networks, and programs from digital attacks.
* **Ethical Hacking:** The authorized practice of bypassing system security to identify potential data breaches and threats in a network.
* **Kali Linux:** The industry-standard Linux distribution designed for digital forensics and penetration testing.

---

## 📚 Resources

### 🔧 Setup & Tools
* **Kali Linux Setup:** [Virtual Machine Guide](https://www.kali.org/docs/virtualization/) | [Desktop & Laptop Guide](https://www.kali.org/docs/installation/)

### 📖 Read or Watch
* [What is Cybersecurity?](https://www.cisco.com/c/en/us/products/security/what-is-cybersecurity.html)
* [The 5 Types of Cybersecurity](https://www.cisa.gov/)
* [The 5 Most Important Cybersecurity Concepts](https://www.youtube.com/watch?v=lPA8D7_J5t8)
* **The CIA Triad:** Confidentiality, Integrity, and Availability.
* **Risk Management:** Identifying and mitigating security risks.
* **Frameworks:** NIST, ISO, COBIT.

### 🔗 References
* [CISA](https://www.cisa.gov/) (Cybersecurity and Infrastructure Security Agency)
* [NIST](https://www.nist.gov/cyberframework) (National Institute of Standards and Technology)
* [OWASP](https://owasp.org/) (Open Web Application Security Project)
* [SANS Institute](https://www.sans.org/)
* [ISC²](https://www.isc2.org/)

---

## 🎯 Learning Objectives

By the end of this project, you should be able to explain the following concepts clearly:

### General Knowledge
* **What is Cybersecurity?** The practice of defending computers, servers, mobile devices, electronic systems, networks, and data from malicious attacks.
* **The CIA Triad:** The core principles of security—**Confidentiality** (privacy), **Integrity** (data accuracy), and **Availability** (accessibility).
* **Encryption:** How encoding information prevents unauthorized access.
* **Risk Management:** The process of identifying, assessing, and controlling threats to an organization's capital and earnings.

### Threats & Attacks
* **Cybersecurity Threats:** Malware, ransomware, phishing, Man-in-the-Middle (MitM), Denial of Service (DoS).
* **Virus vs. Worm:** * *Virus:* Needs a host program to run and replicate.
    * *Worm:* Can replicate and spread independently without a host.
* **Social Engineering:** Manipulating people into giving up confidential information (e.g., Phishing, Pretexting).

### Defense & Governance
* **Security Policies & Frameworks:** How structured guidelines (like NIST or ISO 27001) help organizations maintain a strong security posture.
* **OWASP Top Ten:** The standard awareness document for developers and web application security, listing the most critical security risks.
* **Access Control:** The selective restriction of access to a place or other resource (Authentication vs. Authorization).
* **Multi-Factor Authentication (MFA):** Enhancing security by requiring multiple forms of verification (Something you know, have, or are).
* **Network Security:** Firewalls, VPNs, IDS/IPS, and network segmentation.

---

## ⚙️ Requirements

### General
* **Environment:** All scripts and files will be tested on **Kali Linux 2023.2**.
* **Editors:** `vi`, `vim`, `emacs`.
* **Script Format:**
    * All Bash scripts must start with exactly `#!/bin/bash`.
    * All files must end with a new line.
    * **Length:** Scripts must be **less than 2 lines long** (`wc -l file` should return `<= 2`).
* **Constraints:**
    * You are **NOT** allowed to use backticks, `&&`, `||`, or `;`.
    * You are **NOT** allowed to use `printf`.
    * The IP range must be substituted using the argument `$1`.
* **Style:** Code must follow the **Betty** style and will be checked using `betty-style.pl` and `betty-doc.pl`.

---

## 📂 Repository Information

* **GitHub Repository:** `holbertonschool-cyber_security`
* **Directory:** `introduction_to_cyber_security`
