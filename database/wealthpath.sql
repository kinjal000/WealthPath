-- Create Database
CREATE DATABASE IF NOT EXISTS wealthpath;

USE wealthpath;

CREATE TABLE IF NOT EXISTS users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(100),
    role VARCHAR(50)
);

INSERT INTO users(name,email,password,role)
VALUES
('Admin','admin@gmail.com','admin123','Admin');

CREATE TABLE IF NOT EXISTS clients(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(20),
    email VARCHAR(100),
    city VARCHAR(100)
);

INSERT INTO clients(name,phone,email,city)
VALUES
('Rahul Sharma','9876543210','rahul@gmail.com','Mumbai'),
('Priya Patel','9876501234','priya@gmail.com','Pune');

CREATE TABLE IF NOT EXISTS investments(
    id INT AUTO_INCREMENT PRIMARY KEY,
    client_name VARCHAR(100),
    investment_type VARCHAR(100),
    amount DOUBLE,
    risk_level VARCHAR(50)
);

INSERT INTO investments(client_name,investment_type,amount,risk_level)
VALUES
('Rahul Sharma','Mutual Fund',50000,'Medium'),
('Priya Patel','Stocks',120000,'High');

SHOW TABLES;

SELECT * FROM users;

SELECT * FROM clients;

SELECT * FROM investments;

