-- Creation of the table second_table
CREATE TABLE IF NOT EXISTS second_table
(
	id INT,
	name VARCHAR(256),
	score INT
);
-- Add some records
INSERT INTO second_table
VALUES
(1, "Jhon", 10),
(2, "Alex", 3),
(3, "Bob", 14),
(4, "George", 8);
