# SQL & NoSQL Injection

Injection vulnerabilities consistently rank among the most critical web security risks. This project explores the mechanics of **SQL Injection (SQLi)** and **NoSQL Injection**, focusing on how attackers bypass authentication, exfiltrate data, and manipulate database logic. You will learn to identify these vulnerabilities and, more importantly, how to implement robust defenses like parameterized queries and input validation.

---

## 📚 Resources

**Read or watch:**

* [SQL vs. NoSQL: What’s the difference?](https://www.mongodb.com/nosql-explained/nosql-vs-sql)
* [Understanding SQL Injection](https://portswigger.net/web-security/sql-injection)
* [SQL Injection Knowledge Base](https://portswigger.net/web-security/sql-injection/cheat-sheet)
* [A Comprehensive Guide To NoSQL Injection](https://www.imperva.com/learn/application-security/nosql-injection/)
* NoSQL Injections: Overview and Prevention
* SQL vs NoSQL or MySQL vs MongoDB
* Preventing SQL Injection Vulnerabilities

**References:**

* [OWASP: SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
* [Hacker Tricks: SQL Injection](https://www.google.com/search?q=https://book.hacktricks.xyz/pentesting-web/sql-injection)
* [Hacker Tricks: NoSQL Injection](https://www.google.com/search?q=https://book.hacktricks.xyz/pentesting-web/nosql-injection)
* [CWE-89: SQL Injection](https://cwe.mitre.org/data/definitions/89.html)
* [CWE-943: Improper Neutralization of Special Elements in NoSQL Queries](https://cwe.mitre.org/data/definitions/943.html)

---

## 🎯 Learning Objectives

At the end of this project, you are expected to be able to explain the following concepts clearly without the help of Google:

### SQL Injection (SQLi)

* What **SQL Injection** is and its associated risks.
* How a **UNION attack** works to retrieve data from other tables.
* The mechanics of **Blind SQL Injection** (Boolean-based vs. Time-based).
* The role of the `LIMIT` clause in exfiltrating data.
* How to use **Escaping User Input** (and its limitations).

### NoSQL Injection

* How **NoSQL Injection** differs from traditional SQLi.
* How NoSQL Injection occurs specifically in **MongoDB** (e.g., using `$gt` or `$ne` operators).
* Identification of **NoSQL Injection Attack Vectors**.

### Prevention & Mitigation

* What a **Parameterized Query** (Prepared Statement) is and why it's the gold standard for defense.
* The role of **ORMs** (Object-Relational Mappers) in preventing injections.
* The importance of **Input Validation** and using **Regular Expressions**.
* What **Stored Procedures** are in SQL and their impact on security.

---

## ⚙️ Requirements

### General

* **Allowed editors:** `vi`, `vim`, `emacs`.
* **Environment:** All your scripts will be tested on **Kali Linux**.
* **Target:** Your focus will be on the target machine: `cyber_websec_0x01`.
* **Constraint:** For this project, you are **NOT allowed to use `sqlmap**`. All injections must be performed manually.
* **README:** A `README.md` file at the root of the folder of the project is mandatory.

### Script Constraints

* **Length:** All your scripts must be **exactly one line long**.
* **Validation:** `$ wc -l file` must print `1`.
* **Formatting:** All your files must end with a new line.

---

## 🛠️ Comparison Overview

| Feature | SQL Injection | NoSQL Injection |
| --- | --- | --- |
| **Primary Target** | Relational DBs (MySQL, PostgreSQL) | Document/Key-Value DBs (MongoDB, CouchDB) |
| **Common Syntax** | `' OR '1'='1` | `{"$gt": ""}` |
| **Technique** | Breaking out of string quotes | Manipulating object logic/operators |
| **Primary Defense** | Prepared Statements | Schema validation & Type checking |

---

## 📋 Repository Information

* **GitHub repository:** `holbertonschool-cyber_security`
* **Directory:** `web_application_security/0x01_sql_nosql_injection`
