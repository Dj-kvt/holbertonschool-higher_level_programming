-- Create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- command for use the base
USE hbtn_0d_usa;

-- Create table if already  not exist
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL,
    state_id INT,
    FOREIGN KEY (state_id) REFERENCES states(id)
);