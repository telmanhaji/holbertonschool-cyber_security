# Linux Privilege Escalation

## 📖 Introduction

Establishing initial entry into a Linux target environment is rarely the end of a security assessment. True impact is demonstrated during the **Privilege Escalation** phase, where an operator moves from a highly restricted initial access foothold to an administrative account (such as `root`). This transition is critical for accessing protected assets, evaluating cross-host lateral visibility, and demonstrating complete systemic compromise.

Rather than chasing rare or highly theoretical capture-the-flag (CTF) edge cases, this repository focuses on identifying and abusing **real-world misconfigurations, flaws, and permission oversights** commonly encountered in enterprise systems.

---

## 🎯 Learning Objectives

By the completion of this module, the following foundational and tactical system-level escalation techniques are mastered without external assistance:

* **System Enumeration:** Running manual checks and automated scripts to systematically gather operating system patch levels, ambient environment paths, operational software services, and cron configurations.
* **Kernel & Service Subversion:** Recognizing out-of-date system kernels vulnerable to public exploits (e.g., Dirty COW) and targeting background daemons executing under high-privilege scopes.
* **Access Control Abuse:** Locating and weaponizing misconfigured binary privileges (**SUID/SGID** tags), structural filesystem flaws (world-writable paths), and over-permissive `sudoers` definitions.
* **Library Manipulation:** Hijacking shared object loading paths by manipulating environment variables like `LD_PRELOAD` or `LD_LIBRARY_PATH`.
* **Credential Reclamation:** Harvesting cleartext tokens or hashed credentials leaked inside files, configurations, or shell histories, then processing them via localized cracking suites (`John the Ripper`).
* **Operational Monitoring:** Utilizing native network and process inspection binaries (`ss`, `netstat`, `ps`, `tcpdump`) to audit live target activity and track running processes.

---

## ⚙️ Technical Requirements & Guidelines

To ensure systemic portability and maintain high operational standards, all scripts, logs, and evidence gathered follow these strict requirements:

* **Execution Environments:** Tested and validated on standard, active Linux distributions (such as Ubuntu or Kali Linux).
* **Workspace Documentation:** Every exploit verification sequence documents its findings natively. High-level summaries are cataloged inside `README.md`, while detailed stdout logs are channeled directly into a dedicated `results.md` file.
* **Code Craftsmanship:** Custom script components require detailed, descriptive comment strings explaining the purpose of each system routing call.
* **Credential Handling:** The use of hardcoded security parameters or static credentials within scripts is strictly banned; variable ingestion or secure environmental mappings must be used instead.
* **Tool Permissions:** Automated diagnostic utilities, exploit code, and reference resources are limited to:
* **LinPEAS** & **LinEnum** (Automated discovery assistance)
* **GTFOBins** (Binary capability mapping references)
* **ExploitDB** & **Linux Exploit Suggester** (Kernel matching verification)
* **Nmap** (Network interface auditing)



---

## 🔬 Target Environment & Connectivity

The laboratory platform maps an assumed-breach vector using an isolated Linux container:

* **Target System Identifier:** `cyber shell 0x02 linux privesc task1`
* **Connection String:** `ssh user@<YOUR_CONTAINER_IP>`
* **Authentication Token:** `user`

---

## 📂 Repository Layout

```
holbertonschool-cyber_security/
└── privilege_escalation_security_shells/
    └── 0x01_linux_privesc/
        ├── 0-flag.txt
        └── results.md

```

---

## ⚡ Active Attack Configurations & Tasks

### Task 0: Flag File Privilege Escalation (Sudo Choom Abuse)

#### Description & Mechanics

The objective is to gain administrative access to the filesystem to read the highly restricted flag file located under `/root/flag.txt`. System enumeration reveals that the low-privilege `user` account holds specialized, unauthenticated `sudo` execution permissions over the native system management command `/usr/bin/choom`.

The `choom` binary is natively designed to display or alter the Out-Of-Memory (OOM) killer score adjustment configurations for running processes. However, when an administrative wrapper tool like `sudo` allows users to invoke `choom` with arbitrary inputs, an attacker can pass execution strings (such as spawning a shell) directly through the binary. Because `choom` inherits the execution context of the `sudo` call, the spawned child process runs with full `root` system authority.

```
[ Restricted User Shell ] ──( Invokes: sudo choom -n 0 /bin/sh )──> [ Sudo Engine Checks Policy ]
                                                                                   │
                                                                       ( Authorized Exec as Root )
                                                                                   │
                                                                                   ▼
                                                                        [ Root Shell Granted ]

```

#### Operational Exploitation Steps

1. **Initial Enumeration:** Authenticate via SSH and verify allowed user capabilities:
```bash
sudo -l

```


*Confirm that `/usr/bin/choom` appears in the allowlist without requiring a password.*
2. **Exploit Execution:** Leverage the tool to execute a standard shell binary while passing OOM parameters:
```bash
sudo choom -n 0 /bin/sh

```


3. **Flag Capture:** Once root privileges are verified via `whoami`, read the target asset:
```bash
cat /root/flag.txt

```



> [!NOTE]
> Per target submission parameters, if the root file outputs a structured wrapper string such as `CTF{privilege_escalation_via_sudo_choom_579eea17d42c385d4be6a0750c6b5562}`, isolate and extract **only** the cryptographic hash within the brackets for your final answer submission:
> `579eea17d42c385d4be6a0750c6b5562`

#### Deliverable Mapping

* **File Containing Extracted Hash:** `privilege_escalation_security_shells/0x01_linux_privesc/0-flag.txt`

---

## 🛡️ Defensive Hardening Matrix (Remediation Design)

To secure enterprise Linux environments against systemic privilege escalation vectors, blue teams must enforce strict, proactive infrastructure policies:

> [!IMPORTANT]
> ### 1. Restrict Sudo Configurations
> 
> 
> Avoid granting open execution privileges over system optimization utilities (like `choom`) that allow command breakout sequences. If a utility must be used, enforce rigid argument constraints inside the configuration file (`/etc/sudoers`) instead of allowing wildcard parameter parsing.
> ### 2. Systemic Patching & Update Cycles
> 
> 
> Maintain a structured patch management lifecycle to continuously update system kernels and baseline software services, neutralizing known public exploits.
> ### 3. Minimize World-Writable Permissions
> 
> 
> Periodically audit the local filesystem to discover and fix insecure permissions on system-critical files, cron configurations, and binary execution directories:
> ```bash
> find / -perm -2 -type f 2>/dev/null
> 
> ```
> 
> 

---

## ⚠️ Disclaimer

> [!WARNING]
> This repository is maintained exclusively for ethical security education, authorized infrastructure audits, and academic lab tracking. Targeting external networks or executing exploit scripts against production infrastructure without clear, prior written legal consent is strictly prohibited by law.o
