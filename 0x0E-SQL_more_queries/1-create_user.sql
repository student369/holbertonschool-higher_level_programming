-- Create the user_0d_1 in the database
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Set all the privileges to the user_0d_1
GRANT ALL ON *.* TO 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Refresh the privileges
FLUSH PRIVILEGES;
