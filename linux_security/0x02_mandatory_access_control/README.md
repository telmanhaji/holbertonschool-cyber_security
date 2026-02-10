# Mandatory Access Control

Mandatory Access Control (MAC) is a security strategy that restricts the ability of individual resource owners to grant or deny access to objects in a file system. Unlike Discretionary Access Control (DAC), where users own and control their files, MAC is centrally managed by the system policy. This project explores the implementation of MAC in Linux through **SELinux** and **AppArmor**, focusing on labels, policies, and the principle of least privilege.

---

## 📚 Resources

* [Introduction to Mandatory Access Control (MAC)](https://www.techtarget.com/searchsecurity/definition/mandatory-access-control-MAC)
* [Your visual how-to guide for SELinux policy enforcement](https://www.google.com/search?q=https://www.redhat.com/en/blog/visual-how-guide-selinux-policy-enforcement)
* 5 security technologies to know in Red Hat Enterprise Linux
* [AppArmor: An alternative to SELinux](https://ubuntu.com/tutorials/beginning-apparmor-profile-development)
* Linux Security: MAC, DAC, and RBAC
* [Security-Enhanced Linux for mere mortals](https://www.youtube.com/watch?v=_WOKRaM-HI4)
* AppArmor vs SELinux: What's the Difference?
* `semanage` Command with Examples

**References:**

* [NIST on MAC](https://csrc.nist.gov/glossary/term/mandatory_access_control)
* SELinux Project Wiki & CentOS Documentation
* AppArmor Project Wiki
* [Linux Kernel Capabilities and MAC](https://man7.org/linux/man-pages/man7/capabilities.7.html)
* `man semanage`

---

## 🎯 Learning Objectives

By the end of this project, you should be able to explain the following concepts clearly without the help of a search engine:

### SELinux & AppArmor

* What **MAC** is in the context of Linux security.
* How **SELinux** enforces MAC through labels and policy.
* The architectural differences between **SELinux** (label-based) and **AppArmor** (path-based).
* The concept of an **AppArmor profile** and how to reload it.

### Core Mechanisms

* **Labels:** How file contexts work in SELinux.
* **Security Models:** Type Enforcement (TE), Role-Based Access Control (RBAC), and Multi-Level Security (MLS).
* **Least Privilege:** How MAC limits the blast radius of a compromised process.
* **Capabilities:** The significance of Linux capabilities in fine-grained security.

### Management & Troubleshooting

* Checking SELinux status (`sestatus`) and common management commands.
* Using `semanage` to set file contexts.
* Troubleshooting MAC issues using **audit logs**.

---

## ⚙️ Requirements

### General

* **Environment:** All files will be run on **Kali Linux 2023.2**.
* **Allowed editors:** `vi`, `vim`, `emacs`.
* **Shebang:** The first line of all your files must be exactly `#!/bin/bash`.
* **Script Constraints:**
* All scripts must be **exactly 2 lines long** (`wc -l` should print 2).
* You must substitute the IP range for `$1`.
* You are **not allowed** to use `printf`.
* You are **not allowed** to use backticks, `&&`, `||`, or `;`.


* **Style:** Your code must follow the **Betty style**. (Checked using `betty-style.pl` and `betty-doc.pl`).
* **Formatting:** All files must end with a new line and be executable.

---

## 🛠️ Security Framework Comparison

| Feature | SELinux | AppArmor |
| --- | --- | --- |
| **Philosophy** | Rule-based (Everything is denied by default) | Path-based (Protects specific applications) |
| **Complexity** | High (Powerful but steep learning curve) | Moderate (Easier to configure) |
| **Identification** | Inode labels (File contexts) | File system paths |
| **Enforcement** | Kernel-level (LSM) | Kernel-level (LSM) |

---

## 📋 Repository Information

* **GitHub repository:** `holbertonschool-cyber_security`
* **Directory:** `linux_security/0x02_mandatory_access_control`