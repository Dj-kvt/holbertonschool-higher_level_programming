-- Créer la base de données si elle n'existe pas
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Utiliser la base
USE hbtn_0d_usa;

-- Créer la table states si elle n'existe pas
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL,
    state_id INT,
    FOREIGN KEY (state_id) REFERENCES states(id)
);