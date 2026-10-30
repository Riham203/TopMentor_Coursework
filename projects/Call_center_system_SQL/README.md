# 📞 Call Center Management System — Relational Database Project

Hi, I'm **Riham Hussain**, an AI & Data Science Enthusiast! 👋

A normalized relational database system designed to log customer communications, track support tickets, monitor call resolution outcomes, and compute agent performance metrics in enterprise call center environments.

---

## 📌 Features

* **3rd Normal Form (3NF) Architecture:** Structured across 5 core tables (`Departments`, `Agents`, `Customers`, `Support_Tickets`, and `Call_Logs`).
* **Automated Database Triggers:** Utilizes `trg_after_call_insert` to automatically increment agent call tallies and auto-resolve linked support tickets upon resolution.
* **Analytical Reporting Queries:** Pre-built SQL queries for calculating agent handle times, call outcome percentages, and auditing comprehensive customer interaction histories[cite: 7, 8].
* **Cross-Platform Compatibility:** Tested and optimized for **MariaDB** / **MySQL** environments via **XAMPP** and **phpMyAdmin**[cite: 7, 8].

---

## 🛠️ Tech Stack

* **Database Engine:** MySQL / MariaDB (XAMPP Environment)[cite: 7, 8]
* **Management Tool:** phpMyAdmin / Command Line Interface[cite: 7, 8]
* **Query Language:** SQL (DDL, DML, Triggers, Aggregations, Joins)[cite: 7, 8]

---
## 📂 Repository Structure

```text
.
├── call_center_system.sql   # Full SQL script (Schema creation, triggers, sample data, analytics)
├── call_center_system.md    # Detailed database design & technical documentation
├── .gitignore               # Git ignore rules
├── LICENSE                  # MIT License
└── README.md                # Project documentation
```

---

## 🗄️ Database Schema & Architecture
```text
+---------------------+              +---------------------+
|     DEPARTMENTS     |              |      CUSTOMERS      |
+---------------------+              +---------------------+
| department_id (PK)  |<---+         | customer_id (PK)    |<---+
| department_name     |    |         | first_name          |    |
| description         |    |         | last_name           |    |
+---------------------+    |         | phone (UNIQUE)      |    |
                           |         +----------+----------+    |
                           | 1                  | 1             | 1
                           |                    |               |
                           | M                  | M             | M
+---------------------+    |         +----------v----------+    |
|       AGENTS        |    |         |   SUPPORT_TICKETS   |    |
+---------------------+    |         +---------------------+    |
| agent_id (PK)       |<---+         | ticket_id (PK)      |<---+
| first_name          |    |         | customer_id (FK)    |    |
| last_name           |    |         +----------+----------+    |
| email               |    |                    | 1             |
| department_id (FK)  |----+                    |               |
| status              |                         | M             |
| total_calls_handled |                         |               |
+---------------------+                         |               |
           ^                                    |               |
           | 1                                  |               |
           |                                    |               |
           | M                                  v               |
+----------+------------------------------------+---------------+-----+
|                             CALL_LOGS                               |
+---------------------------------------------------------------------+
| call_id (PK)                                                        |
| customer_id (FK) ---------------------------------------------------+
| agent_id (FK)                                                       |
| ticket_id (FK)                                                      |
| call_type                                                           |
| duration_seconds                                                    |
| call_outcome                                                        |
| start_time                                                          |
+---------------------------------------------------------------------+ 
```   
---

## ⚙️ Business Logic & Automated Trigger

The database includes an automated trigger `trg_after_call_insert` that executes operational updates upon inserting a new call record[cite: 7, 8]:

```sql
DELIMITER //
CREATE TRIGGER trg_after_call_insert
AFTER INSERT ON Call_Logs
FOR EACH ROW
BEGIN
    -- Increment call count for the assigned agent
    UPDATE Agents 
    SET total_calls_handled = total_calls_handled + 1
    WHERE agent_id = NEW.agent_id;
    
    -- Auto-resolve support ticket if call outcome is RESOLVED
    IF NEW.ticket_id IS NOT NULL AND NEW.call_outcome = 'RESOLVED' THEN
        UPDATE Support_Tickets 
        SET status = 'RESOLVED'
        WHERE ticket_id = NEW.ticket_id;
    END IF;
END;
//
DELIMITER ;
```

---

## 🚀 Execution Instructions (XAMPP / phpMyAdmin)
1. Open XAMPP Control Panel and start Apache and MySQL.   
2. Navigate to `http://localhost/phpmyadmin` in your browser.   
3. Create a new database named call_center_db[cite: 7, 8].
4. Click Import and upload call_center_system.sql[cite: 7].
5. Alternatively, open the SQL tab in phpMyAdmin, paste the contents of `call_center_system.sql`, set the Delimiter to `//`, and click **Go**[cite: 7].

---

## 📜 License
Distributed under the MIT License. See `LICENSE` for details.
