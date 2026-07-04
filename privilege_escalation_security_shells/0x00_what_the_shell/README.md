# What is the Shell? (Bypassing Restricted Environments)

## 📖 Introduction

In deeply hardened enterprise environments, standard commands are often the first line of defense blocked by administrators. Blacklists, restricted shells (like `rbash`), and filtered inputs are standard industry implementations designed to neutralize unexpected interactions. Getting past them requires far more than simply memorizing alternative command names.

This repository focuses on **thinking beyond the obvious**. It deep-dives into the underlying mechanics of shell parsing engines to bypass stringent string restrictions using native language behaviors. By mastering concepts such as **globbing**, **argument obfuscation**, **environment variable slicing**, and **character substitution**, we exploit the flexibility of the shell itself to execute instructions when typical system binaries are entirely blacklisted.

---

## 🎯 Learning Objectives

By the completion of this project, the following core shell execution mechanics and evasion paradigms are mastered without relying on external documentation:

* **Shell Fundamentals:** Articulating what a shell parser is and why it remains the ultimate gatekeeper for system interaction in both Linux and Windows.
* **Engine Architecture:** Understanding how execution engines like Bash and PowerShell interpret, expand, and execute input streams.
* **Windows Shell Dynamics:** Distinguishing the architectural differences between the legacy `cmd.exe` engine and the object-oriented `.NET` framework routing of PowerShell.
* **Cross-Platform PowerShell:** Explaining how PowerShell Core provides unified automation capabilities across Linux and macOS ecosystems.
* **Evasion & Filter Mapping:** Recognizing how defenders implement string-matching blacklists, and finding structural gaps left open by simplistic filters.

---

## ⚙️ Technical Requirements & Constraints

To maintain strict compliance and force creative execution paths under rigid criteria, all repository deliverables conform to these strict constraints:

* **Testing OS Platform:** Verified and executed inside a native **Kali Linux** deployment.
* **Terminal Text Editors:** Code blocks must be manipulated using console-native utilities (`vi`, `vim`, `emacs`).
* **The 1-Line Constraint:** To emphasize precision engineering, scripts and bypass sequences must be **exactly one line long** (`wc -l file` must yield exactly `1`).
* **POSIX Rules:** Every deliverable payload file must terminate cleanly with a trailing newline character (`\n`) to preserve stream pipeline parsing.
* **Environment Scope:** All testing procedures target the isolated interactive container environment: `cyber shell 0x01 task2`.

---

## 📂 Repository Layout

```
holbertonschool-cyber_security/
└── privilege_escalation_security_shells/
    └── 0x00_what_the_shell/
        └── 1-flag.txt

```

---

## ⚡ Active Attack Configurations & Tasks

### Task 0: Escape the Blacklist and Read the Flag

#### Context & Operational Parameters

The objective is to read the raw contents of a highly secure flag file located at `/home/user/flag`. However, the host container architecture simulates a hardened restriction policy that completely blocks and drops requests containing standard administrative commands, loops, or pipe symbols.

#### Explicitly Restricted Commands & Patterns

> `bash`, `sh`, `zsh`, `SHELL`, `grep`, `vi`, `vim`, `scp`, `ssh`, `awk`, `tar`, `nano`, `pico`, `ed`, `ex`, `gedit`, `emacs`, `kate`, `lime`, `jed`, `find`, `|`, `-`, `echo`, `for`, `while`, `do`, `done`, `if`, `{}`.

#### Bypassing Strategy: The Power of Wildcard Globbing

When a shell engine encounters wildcard character strings (such as `?` or `*`), it does not pass the literal symbol to an execution block. Instead, the shell's **native path expansion engine** interrogates the file system first and automatically expands the pattern into the appropriate system paths before executing the command.

By replacing blacklisted commands and file paths with specific character placeholders, we can force the shell to look up and execute files like `/bin/cat` and `/home/user/flag` without ever explicitly typing their names—bypassing the string-matching filter entirely.

```
[ Attacker Input: /???/c?t /????/????/fl?? ]
                    │
       ( Native Shell Path Expansion )
                    │
                    ▼
[ Transformed Execution: /bin/cat /home/user/flag ]

```

#### Connection Instructions

```bash
# Command to establish connection to the remote lab asset
ssh user@<YOUR_CONTAINER_IP>
# Password token authentication when prompted
user

```

#### Deliverable Mapping

* **File Containing Extracted Flag:** `privilege_escalation_security_shells/0x00_what_the_shell/1-flag.txt`

---

## 🛡️ Defensive Perspective (Remediation)

> [!IMPORTANT]
> This project proves that **string-based blacklists are fundamentally flawed**. A defender cannot list every single permutation of an obfuscated command string.
> To properly secure a restricted shell environment, administrators must apply a **least-privilege allowlist strategy**:
> 1. Move away from `rbash` restrictions and implement comprehensive, kernel-level logging profiles.
> 2. Restrict the available environment path entirely (`PATH=/home/user/bin`) and populate that specific directory only with the exact binaries required for operation.
> 3. Block direct write and execution capabilities within the user's home partition to prevent environment manipulation.
> 
> 

---

## ⚠️ Disclaimer

> [!WARNING]
> This repository is maintained strictly for ethical security education, defensive engineering analysis, and formal academic lab validation. Executing unapproved command injection attempts or bypass techniques against production infrastructure without clear, written organizational consent is strictly illegal.
