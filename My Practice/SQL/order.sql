SELECT * FROM flights ORDER BY duration ASC;

SELECT * FROM flights ORDER BY duration DESC;

SELECT origin, COUNT(*) FROM flights GROUP BY origin;
SELECT origin, COUNT(*) FROM flights GROUP BY origin HAVING COUNT(*) > 1;
SELECT origin, COUNT(*) FROM flights GROUP BY origin HAVING COUNT(origin) > 1;


SELECT destination, COUNT(*) FROM flights GROUP BY destination;