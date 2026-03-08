# Prompt Injections

Prompt Injection is the "SQL Injection of the AI era." As Large Language Models (LLMs) are integrated into applications to process user data and execute actions, they introduce a new attack surface. This project explores how attackers can subvert an LLM's instructions to bypass safety guardrails, exfiltrate data, or perform unauthorized actions, and—most importantly—how developers can build robust, layered defenses to mitigate these risks.

---

## 📚 Resources

**Read or watch:**

* [OWASP LLM01 — Prompt Injection](https://www.google.com/search?q=https://genai.ovh/owasp-llm-top-10/llm01-prompt-injection/)
* [OWASP LLM Prompt Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html)
* OpenAI Discussion: Protecting LLMs from prompt injections and jailbreaks
* [Google Security Blog — Mitigating prompt injection attacks](https://www.google.com/search?q=https://security.googleblog.com/2023/12/how-we-mitigate-prompt-injection.html) (Layered defense)
* A Systematic Evaluation of Prompt Injection and Jailbreak Vulnerabilities in LLMs
* [Palo Alto Networks — What is a prompt injection attack?](https://www.paloaltonetworks.com/cyberpedia/what-is-a-prompt-injection-attack)
* [IBM — How to prevent prompt injection attacks](https://www.ibm.com/think/topics/prompt-injection)

**References:**

* [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)

---

## 🎯 Learning Objectives

By the end of this project, you should be able to explain the following concepts clearly without the help of a search engine:

### Understanding the Threat

* **What is Prompt Injection?** Defining the subversion of an LLM's system instructions via malicious user input.
* **Jailbreaking:** Techniques used to bypass the safety filters and alignment of a model.
* **The "Why":** Why this matters for any system where an LLM has access to sensitive data or external tools (APIs).

### Attack Classes

* **Direct Injection:** The user directly provides a malicious prompt to the model.
* **Indirect Injection:** The model processes a third-party source (like a website or email) that contains hidden malicious instructions.
* **Prompt Smuggling:** Using encoding or obfuscation to hide instructions from simple filters.
* **Roleplay & Jailbreaks:** Forcing the model into a persona (e.g., "DAN") to ignore its rules.

### Defense & Mitigation

* **Instruction Hardening:** Designing prompts that are resilient to manipulation.
* **Prompt Isolation:** Separating system instructions from user-provided data.
* **Runtime Policy Checks:** Using "Guardrail" models to scan inputs and outputs for malicious intent.
* **Monitoring & Schema Enforcement:** Restricting what the LLM can output and how it interacts with external tools.

---

## ⚙️ Requirements

### General

* **Allowed editors:** `vi`, `vim`, `emacs`.
* **Environment:** All your scripts will be tested against the target environment.
* **Target Environment:** `http://cyber_prompt_injection_0x01:5000/`
* **README:** A `README.md` file at the root of the folder of the project is mandatory.

### Script Constraints

* **Length:** All your files must be **exactly one line long**.
* **Validation:** `$ wc -l file` must print `1`.
* **Formatting:** All your files must end with a new line.

---

## 🛠️ Mitigation Patterns

| Strategy | Description |
| --- | --- |
| **Delimiters** | Using clear markers (e.g., `###` or `"""`) to wrap user input within a prompt. |
| **Input Filtering** | Scanning for known attack strings or "jailbreak" patterns before processing. |
| **Least Privilege** | Ensuring the LLM only has access to the specific data and APIs it absolutely needs. |
| **Output Sanitization** | Reviewing the LLM's response before displaying it to the user or executing a command. |

---

## 📋 Repository Information

* **GitHub repository:** `holbertonschool-cyber_security`
* **Directory:** `cyber_prompt_injection`