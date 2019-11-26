-- Create the database hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Create the user_0d_2 in the database
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Set the select privilege in the database hbtn_0d_2
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Refresh the privileges
FLUSH PRIVILEGES;
