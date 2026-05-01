Server-Side Request Forgery
🌐 Project Overview
This module explores Server-Side Request Forgery (SSRF), a critical vulnerability where an attacker induces a server-side application to make requests to an unintended location. Often, these targets are internal-only services or cloud metadata endpoints that are otherwise inaccessible from the outside world.
🎯 Learning Objectives
By the end of this project, you should be able to explain the following concepts fluently without external assistance:
Core Concepts
[ ] What is SSRF? Understanding the fundamental vulnerability.
[ ] Mechanism: How an application can be manipulated to send requests on behalf of the attacker.
[ ] Impact & Risks: Why SSRF is a gateway to internal network scanning and data exfiltration.
Attack & Defense
[ ] Attack Types: Distinguishing between Basic, Blind, and Semi-Blind SSRF.
[ ] Common Scenarios: Exploiting APIs, local file access, and cloud metadata (AWS/Azure/GCP).
[ ] Protection: Implementing allow-lists, network segmentation, and input validation to prevent attacks.
📚 Resources
Theory & Exploitation
Resource
Description
OWASP SSRF Guide
Comprehensive overview of the vulnerability.
SSRF Explained
A breakdown of finding and exploiting SSRF.
API Exploitation
Specific focus on exploiting SSRF within modern APIs.

Defense Manuals
Defense Strategies: How to harden server-side applications.
SSRF Prevention: Mitigation best practices for internal resources.
🛠️ Requirements & Environment
To maintain high standards and avoid the formatting errors encountered in the previous README.md version, follow these strict guidelines.

General Specifications
Target: Focused on Cyber - WebSec 0x08.
Operating System: Tested and verified on Kali Linux.
Editors: Use vi, vim, or emacs.
Technical Constraints
📏 Script Length: Every script must be exactly one line long.
Verification: wc -l file should print 1.
🏁 Termination: All files must end with a new line to ensure POSIX compliance.
🔌 Port Forwarding: All applications are port-forwarded. Pay strict attention to port numbers when redirecting traffic.
📂 Repository Structure
File
Description
README.md
This documentation file.
[Scripts]
Single-line executable scripts for SSRF testing.



