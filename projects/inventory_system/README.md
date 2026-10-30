# Inventory Management System — Database Project Documentation

**Author:** Riham  
**Environment:** XAMPP (MariaDB / MySQL / phpMyAdmin)  
**Date:** September 2026  

---

## 1. Project Overview

The **Inventory Management System** is a normalized relational database designed to track product stock levels, supplier details, categories, and inventory transactions. The system incorporates database constraints, foreign key relationships, automated database triggers, and aggregate reporting queries to simulate a real-world enterprise inventory backend.

---

## 2. Database Schema Architecture

The database comprises **four core tables** structured in 3rd Normal Form (3NF):

```
+------------------+         +------------------+
|    Categories    |         |    Suppliers     |
+------------------+         +------------------+
| category_id (PK) |         | supplier_id (PK) |
| category_name    |         | supplier_name    |
| description      |         | contact_email    |
+--------+---------+         | phone            |
         |                   +--------+---------+
         | 1                          | 1
         |                            |
         | M                          | M
+--------+----------------------------+---------+
|                    Products                   |
+-----------------------------------------------+
| product_id (PK)                               |
| product_name                                  |
| sku (UNIQUE)                                  |
| category_id (FK)                              |
| supplier_id (FK)                              |
| price                                         |
| quantity_in_stock                             |
| reorder_level                                 |
+----------------------+------------------------+
                       | 1
                       |
                       | M
+----------------------+------------------------+
|             Inventory_Transactions            |
+-----------------------------------------------+
| transaction_id (PK)                           |
| product_id (FK)                               |
| transaction_type ('IN', 'OUT', 'ADJUSTMENT')  |
| quantity                                      |
| transaction_date                              |
| notes                                         |
+-----------------------------------------------+
```

### Data Dictionary

1. **`Categories`**: High-level organization for products (e.g., Electronics, Office Supplies).
2. **`Suppliers`**: Contact information for wholesale vendors.
3. **`Products`**: Primary stock table tracking SKUs, unit pricing, current stock levels, and safety thresholds.
4. **`Inventory_Transactions`**: Detailed audit trail logging stock receipts (`IN`), sales/outflows (`OUT`), and manual count reconciliations (`ADJUSTMENT`).

---

## 3. Business Logic & Automation

A database trigger **`trg_after_inventory_transaction`** is attached to the `Inventory_Transactions` table. Whenever a stock movement record is created, the trigger dynamically recalculates and updates the `quantity_in_stock` column in the `Products` table:

```sql
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
```

---

## 4. Analytical & Reporting Queries

The schema includes pre-built SQL queries for business intelligence and inventory auditing:

### Query 1: Low Stock Threshold Alert
Identifies items that fall below their defined reorder level so replenishment orders can be issued automatically.
```sql
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
```

### Query 2: Inventory Valuation Summary
Calculates current total asset value aggregated by product category.
```sql
SELECT 
    c.category_name,
    COUNT(p.product_id) AS total_products,
    SUM(p.quantity_in_stock) AS total_units,
    SUM(p.quantity_in_stock * p.price) AS total_inventory_value
FROM Products p
JOIN Categories c ON p.category_id = c.category_id
GROUP BY c.category_name
ORDER BY total_inventory_value DESC;
```

### Query 3: Stock Movement Audit Log
Generates a historical chronological record of all stock adjustments for auditing.
```sql
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
```

---

## 5. Execution Instructions (XAMPP / phpMyAdmin)

1. Open **XAMPP Control Panel** and start **Apache** and **MySQL**.
2. Navigate to `http://localhost/phpmyadmin` in your web browser.
3. Click **Import** and upload `inventory_system.sql`.
4. Alternatively, open the **SQL** tab, set the Delimiter to `//`, paste the script contents, and click **Go**.
