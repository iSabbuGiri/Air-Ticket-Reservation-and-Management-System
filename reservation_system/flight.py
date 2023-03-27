class Flight:
    def __init__(self, flight_number, airline_name, origin, destination, departure_time, arrival_time):
        self.flight_number = flight_number
        self.airline_name = airline_name
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time

    def get_flight_info(self):
        return f"{self.airline_name} {self.flight_number} from {self.origin} to {self.destination} departs at {self.departure_time} and arrives at {self.arrival_time}"