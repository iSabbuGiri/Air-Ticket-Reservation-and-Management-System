class Seat:
    def __init__(self, seat_number, seat_class, is_available):
        self.seat_number = seat_number
        self.seat_class = seat_class
        self.is_available = is_available

    def get_seat_info(self):
        return f"{self.seat_number} ({self.seat_class}) is {'available' if self.is_available else 'not available'}"    