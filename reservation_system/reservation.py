import pandas as pd
import pickle

class Reservation:   
    def list(self) -> None:
        with open('store/reservations.dat', 'rb') as f:
            data = pickle.load(f)
            df = pd.DataFrame(data)
            print(df)
            
    def create(self, flight: str, customer: str, seat: str) -> None:
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
            
    def update(self, old_reservation: str, flight: str, customer: str, seat: str):
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
            
    def delete(self, old_reservation: str) -> None:
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