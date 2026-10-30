-- ===================================================
-- CALL CENTER MANAGEMENT SYSTEM DATABASE SCRIPT
-- Tested on: XAMPP (MariaDB / MySQL / phpMyAdmin)
-- ===================================================

CREATE DATABASE IF NOT EXISTS call_center_db;
USE call_center_db;

-- ---------------------------------------------------
-- 1. DROP EXISTING TABLES AND TRIGGERS (CLEANUP)
-- ---------------------------------------------------
DROP TRIGGER IF EXISTS trg_after_call_insert;
DROP TABLE IF EXISTS Call_Logs;
DROP TABLE IF EXISTS Support_Tickets;
DROP TABLE IF EXISTS Agents;
DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS Departments;

-- ---------------------------------------------------
-- 2. CREATE TABLES
-- ---------------------------------------------------

-- Departments Table
CREATE TABLE Departments (
    department_id INT PRIMARY KEY AUTO_INCREMENT,
    department_name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT
);

-- Agents Table
CREATE TABLE Agents (
    agent_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    department_id INT,
    status ENUM('AVAILABLE', 'ON_CALL', 'OFFLINE') DEFAULT 'AVAILABLE',
    total_calls_handled INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (department_id) REFERENCES Departments(department_id) ON DELETE SET NULL
);

-- Customers Table
CREATE TABLE Customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone VARCHAR(20) NOT NULL UNIQUE,
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Support Tickets Table
CREATE TABLE Support_Tickets (
    ticket_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    subject VARCHAR(255) NOT NULL,
    status ENUM('OPEN', 'IN_PROGRESS', 'RESOLVED', 'CLOSED') DEFAULT 'OPEN',
    priority ENUM('LOW', 'MEDIUM', 'HIGH', 'URGENT') DEFAULT 'MEDIUM',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE
);

-- Call Logs Table
CREATE TABLE Call_Logs (
    call_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    agent_id INT NOT NULL,
    ticket_id INT NULL,
    call_type ENUM('INBOUND', 'OUTBOUND') NOT NULL,
    start_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    duration_seconds INT NOT NULL CHECK (duration_seconds >= 0),
    call_outcome ENUM('RESOLVED', 'ESCALATED', 'DROPPED', 'FOLLOW_UP_REQUIRED') NOT NULL,
    notes TEXT,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (agent_id) REFERENCES Agents(agent_id) ON DELETE CASCADE,
    FOREIGN KEY (ticket_id) REFERENCES Support_Tickets(ticket_id) ON DELETE SET NULL
);

-- ---------------------------------------------------
-- 3. CREATE AUTOMATED TRIGGER FOR AGENT METRICS
-- ---------------------------------------------------
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

-- ---------------------------------------------------
-- 4. INSERT SAMPLE TEST DATA
-- ---------------------------------------------------

-- Departments
INSERT INTO Departments (department_name, description) VALUES
('Technical Support', 'Handles hardware and software troubleshooting'),
('Billing & Accounts', 'Manages subscriptions, payments, and refunds'),
('General Inquiries', 'Handles product info and general customer questions');

-- Agents
INSERT INTO Agents (first_name, last_name, email, department_id, status) VALUES
('Alex', 'Mercer', 'alex.m@callcenter.com', 1, 'AVAILABLE'),
('Sarah', 'Connor', 'sarah.c@callcenter.com', 2, 'AVAILABLE'),
('David', 'Miller', 'david.m@callcenter.com', 1, 'ON_CALL');

-- Customers
INSERT INTO Customers (first_name, last_name, phone, email) VALUES
('John', 'Doe', '+15550192', 'john.doe@example.com'),
('Jane', 'Smith', '+15550144', 'jane.smith@example.com'),
('Robert', 'Johnson', '+15550188', 'robert.j@example.com');

-- Support Tickets
INSERT INTO Support_Tickets (customer_id, subject, status, priority) VALUES
(1, 'Unable to login to account', 'IN_PROGRESS', 'HIGH'),
(2, 'Incorrect charge on monthly invoice', 'OPEN', 'MEDIUM');

-- Test Call Logs (Trigger updates total_calls_handled and ticket status)
INSERT INTO Call_Logs (customer_id, agent_id, ticket_id, call_type, duration_seconds, call_outcome, notes) 
VALUES (1, 1, 1, 'INBOUND', 340, 'RESOLVED', 'Guided customer through password reset procedure.');

INSERT INTO Call_Logs (customer_id, agent_id, ticket_id, call_type, duration_seconds, call_outcome, notes) 
VALUES (2, 2, 2, 'INBOUND', 180, 'FOLLOW_UP_REQUIRED', 'Customer requested bill refund; escalated to finance team.');

-- ---------------------------------------------------
-- 5. ANALYTICAL QUERIES FOR REPORTING
-- ---------------------------------------------------

-- Query 1: Agent Performance Report (Calls handled & avg call duration in minutes)
SELECT 
    a.agent_id,
    CONCAT(a.first_name, ' ', a.last_name) AS agent_name,
    d.department_name,
    a.total_calls_handled,
    ROUND(AVG(c.duration_seconds) / 60, 2) AS avg_call_duration_mins
FROM Agents a
LEFT JOIN Departments d ON a.department_id = d.department_id
LEFT JOIN Call_Logs c ON a.agent_id = c.agent_id
GROUP BY a.agent_id, agent_name, d.department_name;

-- Query 2: Call Resolution & Outcome Breakdown
SELECT 
    call_outcome,
    COUNT(call_id) AS total_calls,
    ROUND((COUNT(call_id) * 100.0 / (SELECT COUNT(*) FROM Call_Logs)), 2) AS percentage
FROM Call_Logs
GROUP BY call_outcome;

-- Query 3: Complete Customer Call History Log
SELECT 
    cl.call_id,
    CONCAT(cust.first_name, ' ', cust.last_name) AS customer_name,
    cust.phone,
    CONCAT(ag.first_name, ' ', ag.last_name) AS agent_name,
    cl.call_type,
    cl.duration_seconds,
    cl.call_outcome,
    cl.start_time
FROM Call_Logs cl
JOIN Customers cust ON cl.customer_id = cust.customer_id
JOIN Agents ag ON cl.agent_id = ag.agent_id
ORDER BY cl.start_time DESC;