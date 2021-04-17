class Flight:
    def __init__(self, capcity):
        self.capcity = capacity
        self.passengers = []
    def add_passengers(self, name):
        if self.passengers == 0:
            return False
        self.add_passengers.append(name)
        return True
    def open_sets(self):
        return self.capcity - len(self.add_passengers)


# Create a new flight with o=up to 3 passengers
flight = Flight(3)

# Create a list of people
people = ["Harry", "Ron", "Hermione", "Ginny"]

# Attempt to add each person in the list to a flight

for person in people:
    if flight.add_passengers(person):
        print(f"Added {person} to flight successfully")
    else:
        print(f"No available seats for {person}")
