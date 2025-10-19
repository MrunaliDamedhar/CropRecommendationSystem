CREATE DATABASE crop_system;

USE crop_system;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255)
);

CREATE TABLE predictions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100),
    nitrogen FLOAT,
    phosphorus FLOAT,
    potassium FLOAT,
    temperature FLOAT,
    humidity FLOAT,
    ph FLOAT,
    rainfall FLOAT,
    crop VARCHAR(50),
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
