import pandas as pd
import pickle

class Seat:
    # def list(self) -> None:
    #     with open('store/seats.dat', 'rb') as f:
    #         try:
    #             data = pickle.load(f)
    #         except EOFError:
    #             data = {}
                
    #     df = pd.DataFrame(data)
        
    #     if data == {}:
    #         print('No data available.')
    #     else:
    #         print('\n{}\n'.format(df))
    
    def create(self, flight_number: str, seat: str, seat_type: str) -> None:
        with open('store/seats.dat', 'rb') as f:
            try:
                data = pickle.load(f)
            except EOFError:
                 data = {}    
                 
        if flight_number in data:
            data[flight_number]['Seats'].append({
                seat: 0,
                'Seat Type': seat_type
            })
        else:
            data.update({
                flight_number: {
                    'Seats': [{
                        seat: 0,
                        'Seat Type': seat_type
                    }]
                }
            })
            
        with open('store/seats.dat', 'wb') as f:
            data = pickle.dump(data, f)