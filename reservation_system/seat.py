import pandas as pd
import pickle

class Seat:
    def flight_exists(self, flight_number: str) -> bool:
        """Method to check if flight exists."""
        with open('store/flights.dat', 'rb') as f:
            try:
                data = pickle.load(f)
            except EOFError:
                return False
            else:
                for item in data:
                    if flight_number in item['Flight Number']:
                        return True
            return False
    
    def list(self):
        with open('store/seats.dat', 'rb') as f:
            data = pickle.load(f)
            df = pd.DataFrame(data)
            print('\n')
            print(df)
            print('\n')
            
    def create(self, flight_number: str, seat: str) -> None:
        if self.flight_exists(flight_number):
            with open('store/seats.dat', 'rb') as f:
                try:
                    data = pickle.load(f)
                except EOFError:
                    data = []
            
            for item in data:
                if flight_number == item['Flight Number']:
                    item.get('Seats', []).append({
                        seat: 0
                    })
                else:
                    data.append({
                        'Flight Number': flight_number,
                        'Seats': [{
                            seat: 0
                        }] 
                    })  

            with open('store/seats.dat', 'wb') as f:
                pickle.dump(data, f)
        else:
            print('Flight number must be unique.')
            
    def update(self, flight_number: str, old_seat: str, new_seat: str) -> None:
        if self.flight_exists(flight_number):
            with open('store/seats.dat', 'rb') as f:
                try:
                    data = pickle.load(f)
                except EOFError:
                    data = []
                    
            for item in data:
                if flight_number == item['Flight Number']:
                    for seat in item.get('Seats', []):
                        if old_seat == seat['seat']:
                            seat['seat']
                        else:
                            print('Seat does not exist.')
                else:    
                    print('Flight does not exist.')

            with open('store/flights.dat', 'wb') as f:
                pickle.dump(data, f)
        else:
            print('Flight number must be unique.')     
                   
    def delete(self, old_flight_number: str) -> None:
        with open('store/flights.dat', 'rb') as f:
            try:
                data = pickle.load(f)
            except EOFError:
                data = []
                
        for item in data:
            if old_flight_number in item['Flight Number']: 
                del item
            else:
                print('Flight does not exist.')

        with open('store/flights.dat', 'wb') as f:
            pickle.dump(data, f)
            
    
        