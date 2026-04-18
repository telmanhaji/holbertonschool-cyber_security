# 🛡️ Incident Response Report: Project "Unmasking Attackers"

## 1. Introduction
This report provides a detailed analysis of the security breach discovered in the web application logs. The goal of this document is to summarize the incident, outline the steps for mitigation, and establish a protocol for future monitoring.

---

## 2. Incident Report (Key Findings)
After analyzing the `auth.log` and `dmesg` files using custom scripts, we have identified the following:

* **Target System Information:**
    * **OS Version:** Linux version 2.6.24-26-server (Ubuntu 4.2.4).
    * **Vulnerability:** The system is running a version from 2009, which is outdated and lacks modern security patches.
* **Compromised Account:** * The account **"Jax"** was identified as the primary compromised user.
* **Scale of the Attack:**
    * **29 unique IP addresses** successfully gained access to the system. This indicates a large-scale breach.
* **Unauthorized Activity:**
    * **11 new accounts** were created by the attackers, including names like `Aphelios`, `Senna`, `Nidalee`, and `Fido`.
* **Firewall Status:**
    * Only **6 firewall rules** were added to `iptables` during the attack, which was insufficient to block the **29** distinct attackers.

---

## 3. Implementation Plan (Security Measures)
To secure the system and prevent future incidents, we will implement the following measures:

1.  **OS Migration:** Immediate upgrade to a modern, supported operating system (e.g., Ubuntu 24.04 LTS) to fix kernel-level vulnerabilities.
2.  **Account Remediation:**
    * Delete all unauthorized accounts identified in the analysis.
    * Reset passwords and SSH keys for all legitimate administrative accounts.
3.  **SSH Hardening:**
    * Disable password-based authentication.
    * Disable `root` login via SSH.
    * Move SSH service to a non-standard port.
4.  **Automated Defense:** Install and configure **Fail2Ban** to automatically block IPs after multiple failed login attempts.

---

## 4. Monitoring Protocol
To maintain a strong security posture, the following guidelines are established:

* **Log Management:** Implement a centralized logging server to prevent attackers from modifying `auth.log` files locally.
* **Daily Security Audits:** Run automated scripts every 24 hours to detect:
    * Unusual peaks in "Failed password" entries.
    * Creation of new users (`useradd`).
* **Real-time Alerting:** Configure system alerts to notify the security team via email or Slack whenever `sudo` is used or firewall rules are changed.
* **Compliance Checks:** Perform a weekly review of the `/etc/passwd` file to ensure no unauthorized users exist.
