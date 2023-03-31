import pandas as pd
import pickle

class Reservation:
    def validate_reservation(self, reservation_id: str) -> bool:
        """
        Method to check if duplicate reservation exists during creation and update.
        Returns boolean value.
        """
        with open('store/reservations.dat', 'rb') as f:
            try:
                data = pickle.load(f)
            except EOFError:
                return True
            else:
                for item in data:
                    if reservation_id in item['Reservation ID']:
                        return False
            return True
    
    def search(self, customer_name: str, arrival_date: int) -> None:
        """Method to search reservation on the basis of customer name and arrival date"""
        found = []
        with open('store/reservations.dat', 'rb') as f:
            data = pickle.load(f)
            
        for item in data:
            if (item['Customer Name'] == customer_name) and (item['Arrival_Date'] == arrival_date):
                found.append(item) 
                
        if found == []:
            print('No results.')
        else:
            df = pd.DataFrame(found)
            print(df)

    def list(self):
        with open('store/reservations.dat', 'rb') as f:
            data = pickle.load(f)
            df = pd.DataFrame(data)
            print('\n')
            print(df)
            print('\n')
            
    def create(self, reservation_id: str, flight_number: str, customer_name: str, seat_number: str, arrival_date: int) -> None:
        if self.validate_reservation(reservation_id):
            with open('store/reservations.dat', 'rb') as f:
                try:
                    data = pickle.load(f)
                except EOFError:
                    data = []
                    
            data.append(
                {
                    'Reservation ID': reservation_id,
                    'Flight Number': flight_number,
                    'Customer Name': customer_name,
                    'Seat Number': seat_number,
                    'Arrival_Date': arrival_date
                }
            )

            with open('store/reservations.dat', 'wb') as f:
                pickle.dump(data, f)
        else:
            print('Reservation ID must be unique.')
            
    def update(self, old_reservation_id: str, reservation_id: str, flight_number: str, customer_name: str, seat_number: str, arrival_date: int) -> None:
        if self.validate_reservation(reservation_id):
            with open('store/reservations.dat', 'rb') as f:
                try:
                    data = pickle.load(f)
                except EOFError:
                    data = []
                    
            for item in data:
                if old_reservation_id in item['Reservation ID']: 
                    item['Reservation ID'] = reservation_id
                    item['Flight Number'] = flight_number
                    item['Customer Name'] = customer_name
                    item['Seat Number'] = seat_number
                    item['Arrival Date'] = arrival_date
                else:    
                    print('Reservation does not exist.')

            with open('store/reservations.dat', 'wb') as f:
                pickle.dump(data, f)
        else:
            print('Reservation ID must be unique.')     
                   
    def delete(self, old_reservation_id: str) -> None:
        with open('store/reservations.dat', 'rb') as f:
            try:
                data = pickle.load(f)
            except EOFError:
                data = []
                
        for item in data:
            if old_reservation_id in item['Reservation ID']: 
                del item
            else:
                print('Reservation does not exist.')

        with open('store/reservations.dat', 'wb') as f:
            pickle.dump(data, f)

