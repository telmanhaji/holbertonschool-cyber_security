# Permissions, SUID & SGID

In the Linux filesystem, everything is a file, and securing those files is the foundation of system administration. This project explores the **Linux Permission Model**, covering standard read, write, and execute bits, as well as special permissions like **SUID** (Set User ID), **SGID** (Set Group ID), and the **Sticky Bit**. Understanding these concepts is vital for maintaining the principle of least privilege and preventing unauthorized access.

---

## 📚 Resources

**Read or watch:**

* [Permissions](https://www.linux.com/training-tutorials/understanding-linux-file-permissions/)
* [Linux permissions](https://www.google.com/search?q=https://www.geeksforgeeks.org/linux-file-permissions/)
* [Finding Files With SUID and SGID](https://www.google.com/search?q=https://www.tecmint.com/find-files-with-suid-and-sgid-permissions-in-linux/)
* [How to Use SUID and SGID on Linux](https://www.google.com/search?q=https://www.howtogeek.com/651/what-is-suid-and-sgid-on-linux/)
* Understanding Linux Special permissions
* [What Is Umask and How to Use it Effectively](https://www.google.com/search?q=https://www.digitalocean.com/community/tutorials/linux-umask-usage-and-examples)

**man or help:**

* `chmod`, `sudo`, `su`
* `chown`, `chgrp`
* `id`, `groups`
* `adduser`, `useradd`, `addgroup`

---

## 🎯 Learning Objectives

By the end of this project, you should be able to explain the following concepts clearly without the help of a search engine:

### Core Permissions

* Identify the **three user-based permission groups** in Linux (User, Group, Others).
* Explain the usage of the following commands:
* `chmod`: Change file mode bits.
* `sudo` / `su`: Execute as superuser or switch users.
* `chown` / `chgrp`: Change file owner and group.


* Understand the difference between `chown` (ownership) and `chgrp` (group association).
* Define **Umask** and how it determines default permissions for new files.

### Special Permissions

* Understand the purpose of **setuid** (SUID) and **setgid** (SGID).
* Know how to apply and identify these bits on executable files and directories.

### Best Practices

* Recommend strategies for managing file permissions safely.
* Describe methods to audit permission changes on a system.

---

## ⚙️ Requirements

### General

* **Allowed editors:** `vi`, `vim`, `emacs`.
* **Environment:** All scripts will be tested on **Kali Linux**.
* **Shebang:** The first line of all your files must be exactly `#!/bin/bash`.
* **Arguments:** You must substitute the IP range for `$1`.
* **Logic Constraints:** You are **not allowed** to use backticks, `&&`, or `||`.
* **Style:** Your code must follow the **Betty style**. (Checked using `betty-style.pl` and `betty-doc.pl`).
* **Formatting:** * All files must end with a new line.
* All files must be executable.


* **README:** A `README.md` file at the root of the project is mandatory.

---

## 🛠️ Permission Breakdown

| Permission | Symbol | Octal | Effect on File | Effect on Directory |
| --- | --- | --- | --- | --- |
| **Read** | `r` | 4 | View contents | List files inside |
| **Write** | `w` | 2 | Modify contents | Add/Delete files |
| **Execute** | `x` | 1 | Run as program | Enter the directory |
| **SUID** | `s` | 4000 | Run as file owner | N/A |
| **SGID** | `s` | 2000 | Run as file group | New files inherit group |

---

## 📋 Repository Information

* **GitHub repository:** `holbertonschool-cyber_security`
* **Directory:** `linux_security/0x01_permissions_sguid_sgid`