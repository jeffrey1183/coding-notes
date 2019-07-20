import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# Creating a databse engine in line 6. 
# The engine is  an object created by SQL alchemy, this third party library that we're going to be using.
# os.getenv database URL specifies in an environment variable the database URL. The URL of where my database lives.
# In my case, that URL is local host, my own computer. But if you've got a database that's living somewhere else on the internet, that might actually be a URL.

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

# On line 10, we're creating a scope session. When we take our web application to the internet, we have multiple people that are simultaneously trying to use our website at the same time, we want to make sure that the stuff that person A is doing with the database is kept separate from the stuff that person B is doing with the database.
# And so creating different sessions for different people is just a way of managing that.
# We have this object called db which allows us to run SQL commands.

def main():
    flights = db.execute("SELECT origin, destination, duration FROM flights").fetchall()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")

# On line 18, I want a query for all of my flight. In the quotation mark, I can specify whatever SQL command I want to run.
# fetchall query gets all of the results.
# On line 19 to 20, I print the results out.

if __name__ == "__main__":
    main()