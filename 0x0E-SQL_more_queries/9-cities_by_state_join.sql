-- Get the cities and display state information
SELECT c.id, c.name, s.name FROM cities AS c
       LEFT JOIN states AS s ON  c.state_id = s.id;
