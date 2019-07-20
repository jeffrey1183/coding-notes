INSERT INTO flights (origin, destination, duration) VALUES ('New York', 'London', 415);
INSERT INTO flights (origin, destination, duration) VALUES ('Taipei', 'Shanghai', 100);
INSERT INTO flights (origin, destination, duration) VALUES ('Berlin', 'Shanghai', 300);
INSERT INTO flights (origin, destination, duration) VALUES ('Taipei', 'Shanghai', 300);
INSERT INTO flights (origin, destination, duration) VALUES ('Berlin', 'London', 250);


SELECT * FROM flights;

SELECT duration, destination FROM flights;

SELECT * FROM flights WHERE id = 3;

SELECT * FROM flights WHERE origin = 'New York';

SELECT * FROM flights WHERE origin = 'New York' AND id <= 5;
SELECT * FROM flights WHERE origin = 'New York' OR id <= 5;

--LIKE operator, this percents stand in as placeholders, they can represent any text.
SELECT * FROM flights WHERE origin Like 'Ne%';
SELECT * FROM flights WHERE origin Like '%a%';

--IN operator

SELECT * FROM flights WHERE duration IN (100, 300);

-- Capital and lowercase letters influences the results. 
SELECT * FROM flights WHERE origin IN ('New York', 'London'); 

SELECT * FROM flights WHERE duration BETWEEN 100 AND 300;

SELECT * FROM flights WHERE duration NOT IN (100, 300);

-- BETWEEN AND
SELECT * FROM flights WHERE duration BETWEEN 300 AND 1000;

-- SUM function and GROUP BY clause
SELECT SUM(duration) FROM flights GROUP BY destination;
SELECT origin, SUM(duration) FROM flights GROUP BY origin;

-- AVG function

SELECT AVG(duration) FROM flights;
SELECT AVG(duration) FROM flights WHERE origin = 'New York';

-- COUNT function

SELECT COUNT(*) FROM flights;
SELECT COUNT(*) FROM flights WHERE id >3;
SELECT COUNT(*) FROM flights WHERE origin = 'New York';


-- MAX Function, you can find all the records with maximum value for each name using the GROUP BY clause

SELECT MAX(duration) FROM flights;
SELECT origin, MAX(duration) FROM flights GROUP BY origin;

-- MIN Function

SELECT origin, MIN(duration) FROM flights GROUP BY origin;
SELECT MAX(duration), MIN(duration) FROM flights;
