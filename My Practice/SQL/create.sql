  CREATE TABLE flight (
    id SERIAL PRIMARY KEY,
    origin VARCHAR NOT NULL,
    destination VARCHAR NOT NULL,
    duration INTEGER NOT NULL
  );

-- Rename table
ALTER TABLE flight
RENAME TO flights;