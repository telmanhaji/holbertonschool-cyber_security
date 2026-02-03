# Cryptography Basics

Cryptography is the cornerstone of modern digital security. This project covers the fundamental concepts of protecting information through encryption, decryption, and hashing. You will explore how to secure data at rest and in transit, as well as how to use industry-standard tools like **John the Ripper** and **hashcat** to audit and test the strength of cryptographic implementations.

---

## 📚 Resources

**Read or watch:**

* [What is cryptography?](https://www.kaspersky.com/resource-center/definitions/what-is-cryptography)
* The importance of cryptography
* What is cryptography in cyber security?
* [Cryptography](https://en.wikipedia.org/wiki/Cryptography)
* [OpenSSL Official Documentation](https://www.openssl.org/docs/)
* [John The Ripper Hash Formats](https://pentestmonkey.net/cheat-sheet/john-the-ripper-hash-formats)
* [How to use hashcat](https://hashcat.net/wiki/doku.php?id=hashcat)

**References:**

* [John the Ripper (JtR)](https://www.openwall.com/john/)
* [hashcat](https://hashcat.net/hashcat/)

---

## 🎯 Learning Objectives

By the end of this project, you should be able to explain the following concepts clearly, without the help of a search engine:

### Fundamental Concepts

* What **cryptography** is in the context of cybersecurity.
* The critical importance of cryptography in data integrity and confidentiality.
* The difference between **Encryption** (encoding data) and **Decryption** (recovering data).
* Various applications of cryptography in everyday technology (HTTPS, VPNs, etc.).

### Algorithms & Hashing

* What a **hash algorithm** is and its one-way nature.
* What **SHA** (Secure Hash Algorithm) stands for and its common versions (e.g., `sha256`).
* The different types of cryptography: **Symmetric** vs. **Asymmetric**.

### Practical Tooling

* What **John the Ripper** is and how to use it for password auditing.
* Techniques to crack advanced hashes with John the Ripper.
* What **hashcat** is and how to leverage GPU power for high-speed cracking.

---

## ⚙️ Requirements

### General

* **Allowed editors:** `vi`, `vim`, `emacs`.
* **Environment:** All scripts will be tested on **Kali Linux**.
* **Script Constraints:**
* All scripts must be **exactly two lines long** (`wc -l` should print 2).
* You must substitute the IP range for `$1`.
* You are **not allowed** to use backticks, `&&`, `||`, or `;`.


* **Style:** Your code must follow the **Betty style** (checked with `betty-style.pl` and `betty-doc.pl`).
* **Formatting:** * All files must end with a new line.
* The first line of every script must be exactly `#!/bin/bash`.
* All files must be executable.



> **⚠️ Warning:**
> Consistently use **lowercase format** when referring to cryptographic algorithms (e.g., use `sha256`, not `SHA256`). Ensure `$1` is used without quotes to prevent unintended argument type alterations.

---

## 🛠️ Toolset Overview

| Tool | Primary Usage |
| --- | --- |
| **OpenSSL** | A robust, commercial-grade, and full-featured toolkit for the TLS and SSL protocols. |
| **John the Ripper** | A fast password cracker, currently available for many flavors of Unix, Windows, and DOS. |
| **hashcat** | The world's fastest and most advanced password recovery utility. |

---

## 📋 Repository Information

* **GitHub repository:** `holbertonschool-cyber_security`
* **Directory:** `cryptography/0x00_cryptography_basics`