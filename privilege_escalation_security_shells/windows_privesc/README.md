# Windows Privilege Escalation

## 📖 Introduction

Gaining initial access to a Windows system is rarely the end goal of a penetration test or offensive engagement—the ultimate objective lies in the privileges. In enterprise Windows environments, the gap between a low-privileged local domain user and the highest administrative context (`NT AUTHORITY\SYSTEM`) is bridged by structural misconfigurations, operational oversights, and insecure system defaults.

This project-based repository explores the art and science of **Windows Privilege Escalation**. It covers the analysis of Windows internals and the exploitation of common vulnerabilities, including unquoted service paths, token manipulation (`SeImpersonatePrivilege`), weak registry/service permissions, credential exposures in backup structures (SAM/SYSTEM), administrative artifact leaks, and DLL hijacking.

---

## 🎯 Learning Objectives

By completing this module, the following Windows internals and privilege elevation vectors are mastered without external assistance:

* **Credential Harvesting:** Extracting plaintext passwords from unattended installation XML blueprints (`sysprep` relics).
* **Backup & Registry Security:** Retrieving system-wide password hashes by parsing offline backups of the SAM and SYSTEM registry hives.
* **Service & DLL Hijacking:** Abuse of over-permissive service access controls and writable application paths to force elevated executions.
* **Session Logging Hazards:** Auditing PowerShell transcription logs to recover high-value security tokens and command arguments.
* **UAC Bypass & Token Abuse:** Explaining how to bypass User Account Control (UAC) and leverage tokens (e.g., via `JuicyPotato` or `PrintSpoofer`).
* **Defensive Mitigation:** Designing security policies (such as Windows LAPS, least privilege, and registry access controls) to prevent systemic escalation.

---

## ⚙️ Technical Requirements & Guidelines

To maintain standardized testing profiles, all operational elements conform to the following strict criteria:

* **Testing OS Platform:** Verified in a isolated Windows virtualization lab, with attack routing managed from **Kali Linux**.
* **Framework Toolkit:** Allowed tools include PowerShell, Cobalt Strike, Metasploit, and Impacket.
* **Code Standards:** All script files must be documented with descriptive comment strings detailing the specific Windows APIs or utilities invoked.
* **Outputs:** Script operations must output logging traces to standard output, with final validation summaries cataloged inside a local `results.md` file. No hardcoded credentials are permitted in the source.

---

## 📂 Repository Layout

```
holbertonschool-cyber_security/
└── privilege_escalation_security_win/
    └── windows_privsec/
        ├── 0-flag.txt
        ├── extract_password.py
        ├── 1-flag.txt
        ├── 2-flag.txt
        └── 3-flag.txt

```

---

## 🔬 Attack Scenarios & Lab Implementations

### Task 0: Unattended File Credential Extraction

* **Target VM:** `LAB01`
* **Access Credentials:** `student` / `Student`
* **Vulnerability:** Unattended system setup files (e.g., `unattend.xml`) containing base64-encoded or plaintext administrative passwords are left behind post-deployment.
* **Solution:** Write a Python script (`extract_password.py`) to systematically scan standard system directories, parsing out `<AdministratorPassword>` nodes using regex patterns. Once the script extracts and decodes the password, it initiates a high-privilege context via `runas` to capture the flag on the Admin Desktop.

#### Extract & Decode Script Preview (`extract_password.py`)

```python
#!/usr/bin/env python3
import os
import re
import base64

# Common pathways for Windows unattended configuration assets
paths = [
    r"C:\Windows\Panther\Unattend.xml",
    r"C:\Windows\Panther\unattend.txt",
    r"C:\Windows\System32\Sysprep\unattend.xml",
    r"C:\unattend.xml"
]

for path in paths:
    if os.path.exists(path):
        print(f"[*] Analyzing unattended configuration file: {path}")
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            # Match administrator credentials inside XML tags
            match = re.search(r"<AdministratorPassword>.*?<Value>(.*?)</Value>", content)
            if match:
                raw_pass = match.group(1)
                # Decode base64 strings if Windows flag specifies base64 encoding
                try:
                    decoded = base64.b64decode(raw_pass).decode("utf-8")
                    print(f"[+] Recovered Plaintext Password: {decoded}")
                except Exception:
                    print(f"[+] Recovered Plaintext Password: {raw_pass}")

```

* **Deliverable Path:** `windows_privsec/0-flag.txt`

---

### Task 1: Abuse of SAM & SYSTEM Backup Files

* **Target VM:** `LAB02`
* **Access Credentials:** `Sammy` / `Sammy`
* **Vulnerability:** Weak file permissions allowing restricted users to read volume shadow copies or backup copies of the local SAM and SYSTEM registry hives.
* **Solution:** 1. Audit target vulnerabilities using the `PrivCheck` PowerShell helper script.
2. Locate exposed SAM and SYSTEM backups (such as system restore volumes or `Windows\Repair` folders).
3. Extract the SAM and SYSTEM registry archives, and copy them to your Kali Linux terminal.
4. Use Impacket's `secretsdump.py` script offline to extract local administrator NTLM hashes:
```bash
impacket-secretsdump -sam SAM -system SYSTEM local

```


5. Authenticate via Pass-the-Hash (PtH) to establish an administrative session and retrieve the flag.


* **Deliverable Path:** `windows_privsec/1-flag.txt`

---

### Task 2: Service Hijacking & Weak DLL Permissions

* **Target VM:** `LAB03`
* **Access Credentials:** `student` / `Student`
* **Vulnerability:** A highly privileged service loads a missing or writable DLL dependency from an unquoted directory path where low-privilege users have write access.
* **Solution:** 1. Execute the `privcheck` audit on the target to locate high-privilege services with write permissions over execution paths.
2. Identify a writable path under the targeted application folder.
3. Compile a custom C++ DLL (such as a replacement for `SprintCSP.dll`) configured to execute local system modifications when initialized.
4. Deploy the compiled binary to the writable application directory.
5. Force-trigger DLL resolution through RPC functions using `WIN10RpcClient.exe` to execute the code with `SYSTEM` authority and retrieve the flag from the administrative desktop:
```cmd
WIN10RpcClient.exe

```


* **Deliverable Path:** `windows_privsec/2-flag.txt`

---

### Task 3: PowerShell Transcript Auditing

* **Target VM:** `LAB04`
* **Access Credentials:** `student` / `Student`
* **Vulnerability:** Over-permissive logging settings. Active PowerShell transcription logs capture full command-line inputs, cleartext parameters, and sensitive outputs from high-privilege administrative sessions.
* **Solution:** 1. Enumerate standard and custom log storage locations to locate PowerShell transcript logs.
2. Parse the transcript files for exposed session history, administrative secrets, and sensitive commands to locate the hidden flag.
* **Deliverable Path:** `windows_privsec/3-flag.txt`

---

## 🛡️ Defensive Hardening & Mitigations

To defend enterprise Windows architectures against these escalation vectors, administrators should apply the following defensive controls:

> [!IMPORTANT]
> ### 1. Secure Unattended Files
> 
> 
> Immediately delete or secure configuration templates (such as `unattend.xml` or `sysprep.inf`) post-deployment once setup processes are complete.
> ### 2. Restrict Directory Permissions & Enforce Path Quotes
> 
> 
> * Enforce strict Access Control Lists (ACLs) to prevent standard users from writing files to application execution folders or service paths.
> * Always enclose service binary paths containing spaces in double quotes (e.g., `"C:\Program Files\App\service.exe"`) to block unquoted service path execution hijack vectors.
> 
> 
> ### 3. Apply Strong Registry & SAM Access Protections
> 
> 
> Prevent non-administrative users from reading configuration hives or system backups, and restrict remote access to SAM/SYSTEM resources.

---

## ⚠️ Disclaimer

> [!WARNING]
> This repository is maintained strictly for ethical hacking education, verified professional training courses, and authorized security assessments. Operating security tools or attempting privilege escalation against external targets without explicit, prior written legal consent is strictly illegal.
