-- Get the 3 top of the max tempreature and the state
SELECT state, MAX(value) AS max_temp FROM temperatures
GROUP BY state ORDER BY state LIMIT 3;
