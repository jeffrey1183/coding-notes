import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


def main():
    f = open("flights.csv")
    reader = csv.reader(f)
    for origin, destination, duration in reader:
        db.execute("INSERT INTO flights (origin, destination, duration) VALUES (:origin, :destination, :duration)",
            {"origin": origin, "destination": destination, "duration": duration})
        print(f"Added flight from {origin} to {destination} lasting {duration} minutes")
    db.commit()

# We're going to insert into flights origin, destination, duration values and I want to fill in those blanks later.
# SQLalchemy supports the placeholders for this purpose. The syntax of colon plus origin means that this is a placeholder for the origin.
# After a comma, I'm providing a Python dictionary, which tells the query what to fill in to each of those individual placeholders. So in the origin placeholder, fill in the string of origin.
# At the end then you need to tell my database db.commit, meaning save the changes that I just made.

