-- Lists all records from second_table that have a name, ordered by score descending
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
