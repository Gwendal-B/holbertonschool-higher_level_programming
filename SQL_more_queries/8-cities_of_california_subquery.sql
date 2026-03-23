-- Lists all cities of California from the database hbtn_0d_usa using a subquery
SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY id ASC;
