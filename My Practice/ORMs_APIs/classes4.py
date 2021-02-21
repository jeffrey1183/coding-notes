class Flight:

    counter = 1

    def __init__(self, orgin, destination, duration):

        # Keep track of id number.
        self.id = Flight.counter
        Flight.counter += 1

        # Keep track of passengers.
        self.passengers = []

        # Details about flight.
        self.orgin = orgin
        self.destination = destination
        self.duration duration
    
    def print_info(self):
        print(f"Flight origin:{origin}")
        print(f"Flight destination:{destination}")
        print(f"Flight duration:{duration}")

        print()
        print("Passengers:")
        for passengers in self.passengers:
            print(f"{passenger.name}")
    
    def delay(self, amount):
        self.duration += amount
    # p is just going to be a Passenger object.

    def add_passenger(self, p):
        self.passengers.append(p)
        p.flight_id = self.id

class Passenger:

    # Keeping track of passenger's name.
    
    def __init__(self, name):
        self.name = name
    
def main():

    # Create flight.
    f1 = Flight(orgin="New York", destination="Paris", duration=540)

    # Create passengers
    alice = Passenger(name="Alice")
    bob = Passenger(name="Bob")

    # Add passengers
    f1.add_passenger(alice)
    f1.add_passenger(bob)

    f1.print_info()


if __name__ == "__main__":
    main()


