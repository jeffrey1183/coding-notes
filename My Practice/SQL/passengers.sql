CREATE TABLE passengers(
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    flight_id INTEGER REFERENCES flights
);

-- The "REFERENCES" helps to enforce constraints to make sure that I can't do something. Please check the detail in the link: https://youtu.be/Eda-NmcE5mQ?t=2804

INSERT INTO passengers (name, flight_id) VALUES ('Alice', 1);
INSERT INTO passengers (name, flight_id) VALUES ('Bob', 1);
INSERT INTO passengers (name, flight_id) VALUES ('Charlie', 2);
INSERT INTO passengers (name, flight_id) VALUES ('Dave', 2);
INSERT INTO passengers (name, flight_id) VALUES ('Erin', 4);
INSERT INTO passengers (name, flight_id) VALUES ('Frank', 6);
INSERT INTO passengers (name, flight_id) VALUES ('Grace', 6);


-- And it would be nice if I didn't need to do two queries.
SELECT * FROM passengers WHERE name = 'Alice';
SELECT * FROM flights WHERE id = 1;


-- In this case, origin and destination are both columns of my flights table. Name is a column of my passengers table.
-- I could join these two queries into one using a special type of syntax called a join. 
-- The last step is telling my query how these two tables are related. what do I want to join them on? What is the relationship between these two tables.
-- The relationship here is that passengers table and get the flight ID column, that should match the ID column of the flights table.--
SELECT origin, destination, name FROM flights JOIN passengers ON passengers.flight_id = flights.id;

SELECT origin, destination, name FROM flights JOIN passengers ON passengers.flight_id = flights.id WHERE name ='Alice';
