-- Créer la base de données si elle n'existe pas
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Créer l'utilisateur s'il n'existe pas
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Donner le privilège SELECT uniquement sur la base hbtn_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';