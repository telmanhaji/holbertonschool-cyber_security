Buffer Overflow
📝 Description
This project explores the fundamentals of memory management, vulnerabilities, and the mechanics of Buffer Overflow attacks. It focuses on how data can exceed its allocated boundary and overwrite adjacent memory, leading to potential system compromises. The practical component involves direct memory manipulation of a running process's heap via the /proc filesystem.
📚 Resources
Theory & Fundamentals
What is a Buffer Overflow?
How Buffer Overflow Attacks Work
Overflow Vulnerabilities & Consequences
Prevention & Mitigation
Mitigation Strategies
Common C Code Vulnerabilities
Technical References
The /proc Filesystem
Buffer Overflow - Types & Prevention
🎯 Learning Objectives
At the conclusion of this project, you should be able to explain the following without the use of external search engines:
[ ] The Basics: What is a buffer and what constitutes an "overflow"?
[ ] Mechanics: How attackers orchestrate these attacks.
[ ] Taxonomy: Different types of buffer overflow attacks (Stack vs. Heap).
[ ] Detection: Methods for identifying vulnerabilities in source code.
[ ] Consequences: The impact on system stability and security.
[ ] Defense: Strategies to prevent and mitigate memory-based exploits.
🛠️ Requirements
Python Scripts
Language: Python 3.4.3
Interpreter: All files interpreted on Ubuntu 14.04 LTS.
Standard: Code must adhere to PEP 8 style guidelines.
Execution: All files must be executable (chmod +x).
Header: First line must be exactly #!/usr/bin/python3.
Editors: vi, vim, or emacs.
Documentation
All modules, classes, and functions must include a descriptive docstring.
Documentation is verified via: python3 -c 'print(__import__("my_module").__doc__)'.
🚀 Tasks
0. Hack the VM
File: read_write_heap.py
Write a Python script that locates a specific string in the heap of a running process and replaces it. This task demonstrates how memory can be accessed and altered via the /proc/[pid]/mem interface.
Usage:

Bash


sudo ./read_write_heap.py <pid> <search_string> <replace_string>


Example Execution:
Terminal 1 (Target Process):

Bash


# Compile and run the dummy C program
gcc -Wall -pedantic -Werror -Wextra main.c -o main
./main
[0] Holberton (0x555e646e02a0)
[1] Holberton (0x555e646e02a0)
...
[92] maroua (0x555e646e02a0)


Terminal 2 (The Exploit):

Bash


# Find the PID and execute the script
ps aux | grep ./main
sudo python3 ./read_write_heap.py 6515 Holberton "maroua"


📂 Repository Information
GitHub: holbertonschool-cyber_security
Directory: linux_security/0x04_buffer_overflow
Primary Script: read_write_heap.py
⚖️ Disclaimer
This repository is for educational purposes within a controlled laboratory environment. Exploiting memory vulnerabilities on systems you do not own is illegal and unethical. Use this knowledge to build more secure and resilient software.

