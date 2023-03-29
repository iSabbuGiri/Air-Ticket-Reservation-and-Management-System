import pandas as pd
import pickle


class Reservation:
    def __init__(self, flight, customer, seat):
        self.flight = flight
        self.customer = customer
        self.seat = seat

    
    def get_reservation_info(self):
        return f"{self.customer.name} has reserved {self.seat.seat_number} on {self.flight.airline_name} {self.flight.flight_number} from {self.flight.origin} to {self.flight.destination}"    
    
    def list(self):
        with open('store/reservations.dat', 'rb') as f:
            data = pickle.load(f)
            df = pd.DataFrame(data)
            print(df)
            
    def create(self, flight, customer, seat):
        with open('store/reservations.dat', 'rb') as f:
            try:
                data = pickle.load(f)
            except EOFError:
                data = []
                
        data.append(
            {
                'Flight': flight,
                'Customer': customer,
                'Seat': seat
            }
        )

        with open('store/reservations.dat', 'wb') as f:
            pickle.dump(data, f)
            
    def update(self, old_reservation, flight, customer, seat):
        with open('store/reservations.dat', 'rb') as f:
            try:
                data = pickle.load(f)
            except EOFError:
                data = []
                
        for item in data:
            if old_reservation == item:
                item['Flight'] = flight
                item['Customer'] = customer
                item['Seat'] = seat

            else:    
                print('Reservation does not exist.')

        with open('store/reservations.dat', 'wb') as f:
            pickle.dump(data, f)
            
    def delete(self, old_reservation):
        with open('store/reservations.dat', 'rb') as f:
            try:
                data = pickle.load(f)
            except EOFError:
                data = []
                
        for item in data:
            if old_reservation == item:
                data.remove(item)
            else:
                print('Reservations does not exist.')

        with open('store/reservations.dat', 'wb') as f:
            pickle.dump(data, f)
            
    
        