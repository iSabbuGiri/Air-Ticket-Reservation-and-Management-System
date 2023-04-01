import pickle

class Seat:
    def flight_exists(self, flight_number: str) -> bool:
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
        
    def create(self, flight_number: str, seat: str, seat_type: str) -> None:
        if self.flight_exists(flight_number):
            with open('store/seats.dat', 'rb') as f:
                try:
                    data = pickle.load(f)
                except EOFError:
                    data = {}    
                    
            if flight_number in data:
                data[flight_number]['Seats'].append({
                    'Name': seat,
                    'Reserved': 0,
                    'Type': seat_type
                })
            else:
                data.update({
                    flight_number: {
                        'Seats': [{
                            'Name': seat,
                            'Reserved': 0, 
                            'Type': seat_type
                        }]
                    }
                })
                
            with open('store/seats.dat', 'wb') as f:
                data = pickle.dump(data, f)
        else:
            print('Flight does not exist.')


          