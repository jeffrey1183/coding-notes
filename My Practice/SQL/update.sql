UPDATE flights
    SET duration = 430
    WHERE origin = 'New York'
    -- where is telling me which rows I want to update. Not all of column called New York
    AND destionation = 'London';


UPDATE flights
    SET origin = 'New York'
    WHERE origin = 'NEW YORK';