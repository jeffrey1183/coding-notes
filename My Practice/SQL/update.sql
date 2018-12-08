UPDATE flights
    SET duration = 430
    WHERE origin = `New York`
-- where is telling me which rows I want to update. Not all of rows
    AND destionation = `London`
