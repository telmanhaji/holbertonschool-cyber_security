# Server-Side Request Forgery (SSRF)

## ⚓ Introduction

Web servers frequently handle data transfers on behalf of users—whether fetching remote files, processing webhooks, or syncing external APIs. However, when a server implicitly trusts user-supplied URLs without rigid validation, it can be weaponized.

**Server-Side Request Forgery (SSRF)** exploits this blind trust, forcing the hosting infrastructure to send arbitrary requests to unintended destinations. This project simulates how an attacker can leverage a web application's own network privileges to bypass peripheral firewalls, pivot into segmented environments, and enumerate internal services like loopback interfaces (`127.0.0.1`), private subnets, or cloud metadata endpoints.

---

## 🎯 Learning Objectives

By the completion of this project, the following core web architecture flaws and exploitation vectors can be comprehensively explained without external documentation:

* **The Mechanics of SSRF:** How applications map incoming input to backend HTTP clients and forward requests inside internal networks.
* **Attack Types:** The technical distinction between **Regular (Basic) SSRF** (where response data is reflected back to the attacker) and **Blind SSRF** (where success must be inferred via out-of-band interaction or time-based variations).
* **Exploitation Scenarios:** Upgrading simple URL manipulation into complete port scanners, internal API fuzzers, and metadata extraction tools.
* **Business & Architectural Impact:** Understanding how SSRF can lead to unauthorized information disclosure, remote code execution (RCE) via unauthenticated internal management consoles, or complete cloud tenant compromise.
* **Defensive Safeguards:** How to structurally design robust security postures using strict URL parsing, application-layer **Allowlists**, and network-level microsegmentation to isolate backend request handlers.

---

## ⚙️ Technical Requirements & Constraints

To maintain standardized execution profiles across testing environments, the following automation constraints are strictly applied:

* **Testing OS:** Verified on a native **Kali Linux** architecture.
* **Text Interfaces:** Authored strictly inside terminal-native text systems (`vi`, `vim`, `emacs`).
* **The 1-Line Constraint:** Payload and automated collection scripts must be **exactly one line long** (`wc -l file` must yield exactly `1`).
* **Formatting:** All deliverables must cleanly end with a trailing newline character (`\n`) for stream execution integrity.
* **Environment Detail:** Every internal laboratory application runs via port-forwarding setups; careful tracking of port mapping contexts is critical during URL redirection vectors.

---

## 🧪 Simulated Case Study: ShopAdmin Vulnerability

### Context & Attack Vector

While auditing the `Cyber - WebSec 0x08` target network, a backend architectural vulnerability was isolated within the application's markdown reduction processing engine. While a perimeter firewall successfully rejects direct external connection requests to the internal administration panels, the restriction is completely subverted because the trusted application server itself makes the queries internally.

```
[ Attacker ] ──( Craft URL Injection )──> [ Public Web Server: Port 3000 ]
                                                   │
                                         ( Forged Internal Request )
                                                   │
                                                   ▼
                                      [ Internal Admin Dashboard ]

```

### Vulnerability Matrix

* **Target Application Architecture:** ShopAdmin Shopping Platform
* **Base Target URL Endpoint:** `http://web0x08.hbtn/`
* **Infrastructure Configuration:** Application is forwarded onto **Port `3000**`
* **Vulnerable Parameter Interface:** `articleApi` (located within the itemized check reduction module)

### Analysis & Proof of Concept (PoC) Workflow

1. Navigate across items on the shopping endpoint to trigger the check reduction option.
2. Intercept the resulting backend web application request using an interception proxy (**Burp Suite**).
3. Inject localized target strings (e.g., pointing towards the loopback interface or isolated backend application structures) directly into the unvalidated `articleApi` parameter field.
4. Exploit the trusted loopback execution to retrieve the protected flag data from the administrative space.

---

## 📂 Repository Layout

```
holbertonschool-cyber_security/
└── web_application_security/
    └── 0x08_ssrf/
        └── 0-flag.txt

```

| File Name | Description |
| --- | --- |
| `0-flag.txt` | Contains the raw, plaintext cryptographic flag retrieved after successfully exploiting the `articleApi` parameter to extract data from the private backend dashboard. |

---

## 🔒 Defensive Engineering (Remediation Strategy)

To effectively secure internal endpoints against SSRF vectors, the application layer should enforce the following defensive rules:

> [!IMPORTANT]
> 1. **Implement Strict Allowlists:** Only permit connections to explicitly verified domains and IP protocols. Avoid relying on blacklists, which are easily bypassed using alternative IP representations (e.g., decimal encoding, `0.0.0.0`, or custom DNS configurations).
> 2. **Enforce Input Validation:** Restrict URL inputs to specific schemes (e.g., forcing `https://` only) to block access via dangerous alternative protocols such as `file://`, `gopher://`, or `dict://`.
> 3. **Isolate Backend Networks:** Implement isolated network zones for application servers that must access public web resources, blocking their ability to connect back to internal network assets.
> 
> 

---

## ⚠️ Disclaimer

> [!WARNING]
> This repository is structured exclusively for educational research, defensive security engineering tracking, and authorized technical evaluation exercises. Unauthorized targeting of live web targets without explicit authorization is strictly illegal.
