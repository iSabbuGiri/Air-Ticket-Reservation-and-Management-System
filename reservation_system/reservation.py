class Reservation:
    def __init__(self, flight, customer, seat):
        self.flight = flight
        self.customer = customer
        self.seat = seat

    def get_reservation_info(self):
        return f"{self.customer.name} has reserved {self.seat.seat_number} on {self.flight.airline_name} {self.flight.flight_number} from {self.flight.origin} to {self.flight.destination}"    