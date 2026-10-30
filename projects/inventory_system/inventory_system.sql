-- ===================================================
-- INVENTORY MANAGEMENT SYSTEM DATABASE SCRIPT
-- Tested on: XAMPP (MariaDB / MySQL / phpMyAdmin)
-- ===================================================

CREATE DATABASE IF NOT EXISTS inventory_db;
USE inventory_db;

-- ---------------------------------------------------
-- 1. DROP EXISTING TABLES AND TRIGGERS (CLEANUP)
-- ---------------------------------------------------
DROP TRIGGER IF EXISTS trg_after_inventory_transaction;
DROP TABLE IF EXISTS Inventory_Transactions;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Suppliers;
DROP TABLE IF EXISTS Categories;

-- ---------------------------------------------------
-- 2. CREATE TABLES
-- ---------------------------------------------------

-- Categories Table
CREATE TABLE Categories (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT
);

-- Suppliers Table
CREATE TABLE Suppliers (
    supplier_id INT PRIMARY KEY AUTO_INCREMENT,
    supplier_name VARCHAR(150) NOT NULL,
    contact_email VARCHAR(100),
    phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Products Table
CREATE TABLE Products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(150) NOT NULL,
    sku VARCHAR(50) UNIQUE NOT NULL,
    category_id INT,
    supplier_id INT,
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0),
    quantity_in_stock INT NOT NULL DEFAULT 0 CHECK (quantity_in_stock >= 0),
    reorder_level INT DEFAULT 10,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES Categories(category_id) ON DELETE SET NULL,
    FOREIGN KEY (supplier_id) REFERENCES Suppliers(supplier_id) ON DELETE SET NULL
);

-- Inventory Transactions Log Table
CREATE TABLE Inventory_Transactions (
    transaction_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT NOT NULL,
    transaction_type ENUM('IN', 'OUT', 'ADJUSTMENT') NOT NULL,
    quantity INT NOT NULL,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    FOREIGN KEY (product_id) REFERENCES Products(product_id) ON DELETE CASCADE
);

-- ---------------------------------------------------
-- 3. CREATE AUTOMATED TRIGGER FOR STOCK UPDATES
-- ---------------------------------------------------
DELIMITER //
CREATE TRIGGER trg_after_inventory_transaction
AFTER INSERT ON Inventory_Transactions
FOR EACH ROW
BEGIN
    IF NEW.transaction_type = 'IN' THEN
        UPDATE Products 
        SET quantity_in_stock = quantity_in_stock + NEW.quantity
        WHERE product_id = NEW.product_id;
    ELSEIF NEW.transaction_type = 'OUT' THEN
        UPDATE Products 
        SET quantity_in_stock = quantity_in_stock - NEW.quantity
        WHERE product_id = NEW.product_id;
    ELSEIF NEW.transaction_type = 'ADJUSTMENT' THEN
        UPDATE Products 
        SET quantity_in_stock = NEW.quantity
        WHERE product_id = NEW.product_id;
    END IF;
END;
//
DELIMITER ;

-- ---------------------------------------------------
-- 4. INSERT SAMPLE TEST DATA
-- ---------------------------------------------------

-- Categories
INSERT INTO Categories (category_name, description) VALUES
('Electronics', 'Hardware, peripherals, and computer accessories'),
('Office Supplies', 'Paper, pens, and desk accessories'),
('Furniture', 'Office chairs, desks, and storage equipment');

-- Suppliers
INSERT INTO Suppliers (supplier_name, contact_email, phone) VALUES
('TechWorld Logistics', 'orders@techworld.com', '555-0192'),
('Global Office Supplies', 'support@globaloffice.com', '555-0144');

-- Products (Initial Stock)
INSERT INTO Products (product_name, sku, category_id, supplier_id, price, quantity_in_stock, reorder_level) VALUES
('Wireless Ergonomic Mouse', 'ELEC-MSO-01', 1, 1, 29.99, 50, 15),
('Mechanical Keyboard', 'ELEC-KBD-02', 1, 1, 89.99, 20, 10),
('A4 Printing Paper (Box)', 'OFF-PPR-01', 2, 2, 35.00, 8, 12),
('Adjustable Desk Chair', 'FURN-CHR-01', 3, 2, 199.99, 5, 3);

-- Test Stock Transactions (Triggers will automatically adjust `quantity_in_stock`)
-- Stock Out (Mouse stock becomes 50 - 10 = 40)
INSERT INTO Inventory_Transactions (product_id, transaction_type, quantity, notes) 
VALUES (1, 'OUT', 10, 'Sale to customer - Order #1001');

-- Stock In / Restock (Keyboard stock becomes 20 + 15 = 35)
INSERT INTO Inventory_Transactions (product_id, transaction_type, quantity, notes) 
VALUES (2, 'IN', 15, 'Supplier Restock - PO #5502');

-- ---------------------------------------------------
-- 5. ANALYTICAL QUERIES FOR REPORTING
-- ---------------------------------------------------

-- Query 1: Low Stock Alert Report (Products at or below reorder level)
SELECT 
    p.product_id,
    p.product_name,
    p.sku,
    p.quantity_in_stock,
    p.reorder_level,
    s.supplier_name,
    s.contact_email
FROM Products p
LEFT JOIN Suppliers s ON p.supplier_id = s.supplier_id
WHERE p.quantity_in_stock <= p.reorder_level;

-- Query 2: Inventory Valuation Summary by Category
SELECT 
    c.category_name,
    COUNT(p.product_id) AS total_products,
    SUM(p.quantity_in_stock) AS total_units,
    SUM(p.quantity_in_stock * p.price) AS total_inventory_value
FROM Products p
JOIN Categories c ON p.category_id = c.category_id
GROUP BY c.category_name
ORDER BY total_inventory_value DESC;

-- Query 3: Stock Movement Audit Log
SELECT 
    t.transaction_id,
    p.product_name,
    t.transaction_type,
    t.quantity,
    t.transaction_date,
    t.notes
FROM Inventory_Transactions t
JOIN Products p ON t.product_id = p.product_id
ORDER BY t.transaction_date DESC;