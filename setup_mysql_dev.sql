-- script to create database and grant user permissions
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbbh_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db. * TO 'hbbh_dev'@'localhost';
GRANT SELECT ON performance_schema. * TO 'hbbh_dev'@'localhost';
FLUSH PRIVILEGES;
