-- This query displays the average temperature (Fahrenheit) by city in descending oreder.

SELECT city, AVG(value) AS average_temperature
FROM temperatures
GROUP BY city
ORDER BY average_temperature DESC;
