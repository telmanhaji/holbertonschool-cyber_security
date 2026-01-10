This project focuses on Nmap Live Host Discovery, a fundamental phase in network security and reconnaissance. You will explore various techniques to identify active devices within a subnetwork without necessarily performing a full port scan. Mastering these methods is essential for mapping network topographies and identifying potential targets or unauthorized devices.

📚 Resources
Read or watch:

Nmap Documentation

Nmap Description

Nmap Options Summary

Target Specification

References:

Host Discovery Techniques

🎯 Learning Objectives
At the end of this project, you are expected to be able to explain the following concepts clearly, without the help of Google:

Core Concepts
What Nmap is and how to use it.

Understanding how Nmap scans work under the hood.

What Subnetworks are and how to enumerate targets within them.

What Nmap can detect (OS, services, etc.).

How to scan a specific IP address and check its ports.

Discovery Techniques
ARP Scan: Local network discovery using Address Resolution Protocol.

ICMP Echo Scan: Traditional "ping" discovery.

ICMP Timestamp & Address Mask Scans: Alternative ICMP queries for bypassing certain filters.

TCP SYN Ping Scan: Discovery using the "half-open" connection method.

TCP ACK Ping Scan: Discovery by sending unexpected ACK packets.

UDP Ping Scan: Discovery by sending packets to highly unlikely UDP ports.

⚙️ Requirements
General
Allowed editors: vi, vim, emacs.

Environment: All scripts will be tested on Kali Linux.

Script Constraints:

All scripts must be exactly two lines long (wc -l should print 2).

You must substitute the IP range for $1.

You are not allowed to use backticks, &&, ||, or ;.

Style: Your code must follow the Betty style (checked with betty-style.pl and betty-doc.pl).

Formatting:

All files must end with a new line.

The first line of every script must be #!/bin/bash.

All files must be executable.

Argument Handling:

Ensure $1 is used without quotes to prevent unintended argument type alterations.

Warning: Do not use " or ' surrounding $1.

📋 Repository Information
GitHub repository: holbertonschool-cyber_security

Directory: network_security/0x04_nmap_live_hosts_discovery

Would you like me to generate the actual two-line code for the ARP scan task to ensure it meets the strict formatting and "No Quotes" requirements?