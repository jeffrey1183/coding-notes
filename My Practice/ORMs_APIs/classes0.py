class Flight:
    def __init__(self, origin, destination, duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration
# When we create a flight, I want to provide, as input, the origin, destination, and duration of the flight.
# And then I want to save that information inside of variables contained within our Flight object.

# Methods in Python classes generally all have self argument. The self argument just refers to the objects that we are working with.
# Origin, destination and duration are other arguments to this method.
# When we create a new flight, those arguments are the different fields that we're going to want to populate. That's the information that we want to store about any particular flight.
# And in order to store them, we'll store them inside of properties inside of our object.
# So self is our object, then we'll set the property self.origin equal to the origin we code in init method.