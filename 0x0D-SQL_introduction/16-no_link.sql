-- This query list all records in the table second_table of the database in MySQL server.

SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
