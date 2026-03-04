-- Lists all cities with their corresponding state name using a JOIN
SELECT cities.id, cities.name, states.name AS state
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
