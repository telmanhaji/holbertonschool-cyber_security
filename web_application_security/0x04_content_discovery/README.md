# Content Discovery

Content Discovery is a fundamental phase in web application security testing. It involves identifying hidden or unlinked resources on a web server—such as directories, files, backup data, and administrative portals—that are not intended for public access. By uncovering these assets, security professionals can map out the full attack surface of an application to identify potential entry points for exploitation.

---

## 📚 Resources

**Read or watch:**

* [Content Discovery](https://www.google.com/search?q=https://www.geeksforgeeks.org/what-is-content-discovery-in-ethical-hacking/)
* [Content Discovery for Web Application Security](https://www.google.com/search?q=https://portswigger.net/burp/documentation/desktop/tools/target/site-map/content-discovery)
* [Content Discovery: Understanding Your Web Attack Surface](https://www.google.com/search?q=https://www.tines.com/blog/content-discovery-attack-surface-management)
* What are the content discovery?
* [OWASP Testing Guide: Content Discovery](https://www.google.com/search?q=https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management_Testing/02-Test_Enumerated_Applications)
* Exploiting: Content Discovery

**References:**

* `dirb` & `nikto`
* `sfuzz` & `wfuzz`
* `gobuster` & `dirbuster`
* `feroxbuster`

---

## 🎯 Learning Objectives

By the end of this project, you should be able to explain the following concepts clearly without the help of a search engine:

### Core Concepts

* What **Content Discovery** is and why it is vital for security auditing.
* What **hidden directories and files** are in the context of web security.
* How **directory bruteforcing** works to reveal unlinked assets.
* The role and application of **fuzzing** in web security.

### Tools & Techniques

* What **wordlists** are and how they drive discovery tools.
* The purpose and usage of automated tools like **Gobuster** and **DirBuster**.
* How **Burp Suite** and **OWASP ZAP** assist in the discovery phase.

---

## ⚙️ Requirements

### General

* **Allowed editors:** `vi`, `vim`, `emacs`.
* **Environment:** All scripts will be tested on **Kali Linux**.
* **Target:** All tasks focus on the target: `Cyber - WebSec 0x04`.
* **README:** A `README.md` file at the root of the project folder is mandatory.

### Script Constraints

* **Length:** All scripts must be **exactly one line long**.
* **Validation:** `$ wc -l [file]` must return `1`.
* **File Ending:** All files must end with a new line.

---

## 🛠️ Toolset Overview

| Tool | Usage |
| --- | --- |
| **Gobuster** | A fast tool used to discover URIs and DNS subdomains using wordlists. |
| **FFUF / Wfuzz** | Flexible web fuzzers used to find hidden parameters and files. |
| **Nikto** | A web server scanner that tests for dangerous files, outdated versions, and specific server problems. |
| **Wordlists** | (e.g., SecLists) Collections of common directory and filenames used for bruteforcing. |

---

## 📋 Repository Information

* **GitHub repository:** `holbertonschool-cyber_security`
* **Directory:** `web_application_security/0x04_content_discovery`