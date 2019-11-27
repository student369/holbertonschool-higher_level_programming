-- Get the cities in california from the second_table table
SELECT id, name FROM cities WHERE state_id=
       (SELECT id FROM states WHERE name=
       	       "California") ORDER BY id;
