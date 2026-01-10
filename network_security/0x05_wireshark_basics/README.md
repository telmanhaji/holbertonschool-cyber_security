Wireshark Basics
 Amateur
 By: Abderrahmen Hidoussi
 Weight: 1
 Your score will be updated as you progress.
Description
For this project, we expect you to look at these concepts:

Wireshark


Resources
Read or watch:
TCP/IP Packet Formats and Ports
Wireshark-Filters
Working With Captured Packets
Examine a captured packet using Wireshark
How to Read Packets in Wireshark
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

What is Wireshark.
How to use Wiresharkfilters .
Analyzing a Package with Wireshark .
Requirements
General
Allowed editors: vi, vim, emacs.
All your scripts will be tested on Kali Linux.
A README.md file, at the root of the folder of the project, is mandatory .
You are free to choose any IP address for testing.
More Info
All your files must contain two lines .
All your files must end with a new line .
All your filters should be written in the txt file format
Example:

cyber-sec@ubuntu$ cat ip_filter.txt
ip.addr==192.0.2.1


cyber-sec@ubuntu$

Install Wireshark.
If Wireshark is not already installed on your terminal

$sudo add-apt-repository ppa:wireshark-dev/stable
$sudo apt update
$sudo apt install wireshark
$sudo usermod -aG wireshark $USER
Basic usage Wireshark.
$ 
wireshark