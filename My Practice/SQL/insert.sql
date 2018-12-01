INSERT INTO flight (origin, destination, duration) VALUES ('New York', 'London', 415);
INSERT INTO flight (origin, destination, duration) VALUES ('Taipei', 'Shanghai', 100);
INSERT INTO flight (origin, destination, duration) VALUES ('Berlin', 'Shanghai', 300);

SELECT * FROM flight;

SELECT duration, destination FROM flight;

SELECT * FROM flight WHERE id = 3;

SELECT * FROM flight WHERE origin = 'New York';

SELECT * FROM flight WHERE origin = 'New York' AND id <= 5;
SELECT * FROM flight WHERE origin = 'New York' OR id <= 5;

SELECT * FROM flight WHERE origin Like 'Ne%';

SELECT * FROM flight WHERE duration IN (100, 300);
SELECT * FROM flight WHERE duration BETWEEN 100 AND 300;

SELECT * FROM flight WHERE duration NOT IN (100, 300);

-- AVG Function

SELECT AVG(duration) FROM flight;

