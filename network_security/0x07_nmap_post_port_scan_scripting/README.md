# Nmap Post Port Scan & Scripting

## 📡 Project Overview
This project focuses on the **Nmap Scripting Engine (NSE)**, one of Nmap's most powerful and flexible features. It allows users to write (and share) simple scripts to automate a wide variety of networking tasks. These scripts are executed in parallel with the speed and efficiency for which Nmap is known.

In this module, we explore how to leverage NSE categories to perform tasks ranging from vulnerability detection and advanced discovery to exploitation and security auditing.

---

## 🎯 Learning Objectives
At the conclusion of this project, you should be able to explain the following concepts without the assistance of external search engines:

### The Nmap Scripting Engine (NSE)
* [ ] **Core Utility:** What is NSE and why is it essential for modern network security?
* [ ] **The Mechanics:** How the engine operates under the hood.
* [ ] **Organization:** How scripts are categorized (e.g., default, safe, intrusive, vuln) and executed.
* [ ] **Automation:** Using command-line arguments to trigger specific NSE scripts.

### Documentation & Scripting
* [ ] **NSE Features:** Practical applications for specialized scripts.
* [ ] **Documentation:** How to utilize **NSEDoc** for writing clear, standardized script documentation.

---

## 📚 Resources

### Official Documentation
| Resource | Description |
| :--- | :--- |
| **Nmap Scripting Engine** | The official guide to NSE. |
| **NSE Categories** | Understanding how scripts are grouped. |
| **NSE Script List** | A comprehensive list of available Nmap scripts. |

### Advanced Guides
* **NSE Usage & Tips:** Enhancing network scans with specialized logic.
* **Scripting Mastery:** Deep dive into Lua-based scripting within the Nmap environment.

---

## 🛠️ Requirements & Constraints
This project follows strict development standards to ensure script precision and portability.

### General Environment
* **Platform:** All scripts are tested on **Kali Linux**.
* **Editors:** `vi`, `vim`, or `emacs`.
* **Style Standard:** All code must adhere to the **Betty Style** (Checked via `betty-style.pl` and `betty-doc.pl`).

### Technical "Hard Mode" Constraints
To ensure mastery over shell fundamentals and command execution, the following rules are active:

* 📏 **Script Length:** All scripts must be **exactly two lines long**.
* 🛑 **Forbidden Syntax:** No backticks, `&&`, `||`, or `;`.
* 🤐 **Zero Echo:** You are **not allowed** to use the `echo` command.
* 🏷️ **Positional Parameters:** You must substitute the target IP range for `$1`.
* ⚠️ **Warning:** Do **not** use quotes around `$1`.
* 🔢 **Port Specification:** Refer to ports by their **numbers**, never by service names.
* 🏁 **Termination:** All files must end with a new line.

---

## 🚀 Usage
Scripts are designed to be executable and perform specific NSE tasks against a target.

```bash
# Example execution
chmod +x your_script.sh
./your_script.sh 192.168.1.0/24
