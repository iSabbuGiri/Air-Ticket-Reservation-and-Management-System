import pandas as pd
import pickle
import uuid

class Reservation:
    def list(self):
        with open('store/reservations.dat', 'rb') as f:
            try:
                data = pickle.load(f)
            except EOFError:
                print('No data available.')
            else:
                if len(data) == 0:
                    print('No data available.')
                else:
                    df = pd.DataFrame(data)
                    print('\n')
                    print(df)
                    print('\n')
            
    def detail(self, id: str) -> None:
        """Method to search reservation on the basis of reservation id"""
        with open('store/reservations.dat', 'rb') as f:
            try:
                data = pickle.load(f)
            except EOFError:
                print('No results found.')
            else:
                if id in data:
                    for key, value in data[id].items():
                        print('{} : {}'.format(key, value))
                        
    def search(self, customer: str) -> None:
        """Search for all reservations using customer ID"""
        res = {}
        with open('store/reservations.dat', 'rb') as f:
            try:
                data = pickle.load(f)
            except EOFError:
                data = {}
        for key, value in data.items():
            if value['Customer'] == customer:
                res.update({
                    key: value
                })
                
        df = pd.DataFrame(res)
        print('\n{}'.format(df))
            
    def create(self, flight_number: str, customer: str, seat_number: str, arrival_date: str) -> None:
        with open('store/reservations.dat', 'rb') as f:
            try:
                data = pickle.load(f)
            except EOFError:
                data = {}
                
        data.update({
            str(uuid.uuid4()): {
                'Flight Number': flight_number,
                'Customer': customer,
                'Seat Number': seat_number,
                'Arrival_Date': arrival_date
            }
        })

        with open('store/reservations.dat', 'wb') as f:
            pickle.dump(data, f)
            
    def update(self, id: str, flight_number: str, customer_name: str, seat_number: str, arrival_date: str) -> None:
        with open('store/reservations.dat', 'rb') as f:
            try:
                data = pickle.load(f)
            except EOFError:
                data = {}
                
        if id in data:
            data[id]['Flight Number'] = flight_number
            data[id]['Customer Name'] = customer_name
            data[id]['Seat Number'] = seat_number
            data[id]['Arrival Date'] = arrival_date

            with open('store/reservations.dat', 'wb') as f:
                pickle.dump(data, f)   
        else:
            print('Reservation does not exist.')  
                   
    def delete(self, id: str) -> None:
        with open('store/reservations.dat', 'rb') as f:
            try:
                data = pickle.load(f)
            except EOFError:
                data = {}
                
        if id in data:
            del data[id]
        else:
            print('Reservation does not exist.')

        with open('store/reservations.dat', 'wb') as f:
            pickle.dump(data, f)

