-- This list all the records with a score that is greater than or equal to 10 in a database.

SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;
