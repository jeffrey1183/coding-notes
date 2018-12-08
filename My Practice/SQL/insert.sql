INSERT INTO flight (origin, destination, duration) VALUES ('New York', 'London', 415);
INSERT INTO flight (origin, destination, duration) VALUES ('Taipei', 'Shanghai', 100);
INSERT INTO flight (origin, destination, duration) VALUES ('Berlin', 'Shanghai', 300);
INSERT INTO flight (origin, destination, duration) VALUES ('Taipei', 'Shanghai', 300);
INSERT INTO flight (origin, destination, duration) VALUES ('Berlin', 'London', 250);


SELECT * FROM flight;

SELECT duration, destination FROM flight;

SELECT * FROM flight WHERE id = 3;

SELECT * FROM flight WHERE origin = 'New York';

SELECT * FROM flight WHERE origin = 'New York' AND id <= 5;
SELECT * FROM flight WHERE origin = 'New York' OR id <= 5;

-- This percents stand in as placeholders, they can represent any text.
SELECT * FROM flight WHERE origin Like 'Ne%';
SELECT * FROM flight WHERE origin Like '%a%';


SELECT * FROM flight WHERE duration IN (100, 300);

-- Capital and lowercase letters influences the results. 
SELECT * FROM flight WHERE origin IN ('New York', 'London'); 


SELECT * FROM flight WHERE duration BETWEEN 100 AND 300;

SELECT * FROM flight WHERE duration NOT IN (100, 300);

-- SUM function and GROUP BY clause
SELECT SUM(duration) FROM flight GROUP BY destination;
SELECT origin, SUM(duration) FROM flight GROUP BY origin;

-- AVG function

SELECT AVG(duration) FROM flight;

-- COUNT function

SELECT COUNT(*) FROM flight;
SELECT COUNT(*) FROM flight WHERE id >3;


-- MAX Function, you can find all the records with maximum value for each name using the GROUP BY clause

SELECT MAX(duration) FROM flight;
SELECT origin, MAX(duration) FROM flight GROUP BY origin;

-- MIN Function

SELECT origin, MIN(duration) FROM flight GROUP BY origin;
SELECT MAX(duration), MIN(duration) FROM flight;
