-- Create the database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use de table hbtn_0d_usa
USE hbtn_0d_usa;
-- Create a table states
CREATE TABLE IF NOT EXISTS states
(
	id INT AUTO_INCREMENT UNIQUE NOT NULL,
	name VARCHAR(256),
	PRIMARY KEY (id)
);
