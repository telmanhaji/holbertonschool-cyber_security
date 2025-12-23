🐧 Linux Security Basics

Welcome to the Linux Security Basics project. This repository focuses on the fundamental security administrative tasks within a Linux environment, specifically using Kali Linux. You will explore the Linux file system hierarchy, process management, network monitoring, and firewall configuration—all critical skills for any cybersecurity professional.

📚 Resources

🔍 Foundational Knowledge

What is the Shell?

What is Kali Linux?

File System Hierarchy Standard (FHS)

Linux File System Explained

🛡️ Security & Networking

Linux Security Commands

Linux Networking Basics

Secure File Transfer (SCP)

UFW Firewall Setup Guide

Iptables vs UFW

🎯 Learning Objectives

By the end of this project, you are expected to be able to explain the following concepts without the help of search engines:

General Linux Concepts

The core structure of the Linux operating system.

The purpose and benefits of the File System Hierarchy Standard (FHS).

Specific purposes of directories (e.g., /etc, /var, /bin).

Security Administration

Methods for protecting sensitive files and directories.

Techniques for monitoring and investigating system activity.

Secure data transfer using encrypted protocols.

Configuration and management of system firewalls.

Command Line Mastery

Process Control: Using ps and kill to audit and terminate malicious processes.

Network Monitoring: Using netstat and ss to identify suspicious connections.

Traffic Analysis: Analyzing behavior with nmap, lynis, and tcpdump.

Firewall Logic: Managing rules with iptables and ufw.

⚙️ Technical Requirements

Environment

OS: All scripts will be tested on Kali Linux.

Editors: vi, vim, emacs.

Scripting Constraints

Shebang: The first line must be exactly #!/bin/bash.

File Length: Every script must be exactly 2 lines long (wc -l should return 2).

Substitution: Use $1 for IP range substitutions.

Format: All files must end with a new line.

Permissions: All files must be executable (chmod +u+x).

Code Style & Integrity

Betty Style: Code must pass betty-style.pl and betty-doc.pl.

Forbidden Syntax: You are NOT allowed to use:

Backticks (`)

Logical operators (&& or ||)

Semicolons (;)

📂 Repository Structure

File

Description

README.md

Project overview and documentation.

*.sh

Executable Bash scripts following strict 2-line constraints.

📝 Coding Standard

This project adheres to the Betty Style, a coding standard used to ensure readability and maintainability. Ensure your documentation is thorough and matches the required headers for script auditing.

# Example check command:
./betty-style.pl your_script.sh
./betty-doc.pl your_script.sh
