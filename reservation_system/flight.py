import pandas as pd
import pickle
from typing import Type

class Flight:
    def validate_flight(self, flight_number: str) -> bool:
        """
        Method to check if duplicate flight exists during creation and update.
        Returns boolean value.
        """
        with open('store/flights.dat', 'rb') as f:
            try:
                data = pickle.load(f)
            except EOFError:
                return True
            else:
                for item in data:
                    if flight_number in item['Flight Number']:
                        return False
            return True
        
    def search(self, origin: str, destination: str) -> None:
        """Method to search flights on the basis of source and destination."""
        found = []
        with open('store/flights.dat', 'rb') as f:
            data = pickle.load(f)
            
        for item in data:
            if (item['Origin'] == origin) and (item['Destination'] == destination):
                found.append(item)
                
        if found == []:
            print('No results.')
        else:
            df = pd.DataFrame(found)
            print(df)
    
    def list(self) -> None:
        with open('store/flights.dat', 'rb') as f:
            data = pickle.load(f)
        df = pd.DataFrame(data)
        print('\n{}\n'.format(df))
    
    def detail(self, flight_number) -> None:
        pass
            
    def create(self, flight_number: str, airline_name: str, origin: str, destination: str, departure_time: str, arrival_time: str) -> None:
        if self.validate_flight(flight_number):
            with open('store/flights.dat', 'rb') as f:
                try:
                    data = pickle.load(f)
                except EOFError:
                    data = []
                    
            data.append(
                {
                    'Flight Number': flight_number,
                    'Airline Name': airline_name,
                    'Origin': origin,
                    'Destination': destination,
                    'Departure Time': departure_time,
                    'Arrival Time': arrival_time
                }
            )

            with open('store/flights.dat', 'wb') as f:
                pickle.dump(data, f)
        else:
            print('Flight number must be unique.')
            
    def update(self, old_flight_number: str, flight_number: str, airline_name: str, origin: str, destination: str, departure_time: str, arrival_time: str) -> None:
        if self.validate_flight(flight_number):
            with open('store/flights.dat', 'rb') as f:
                try:
                    data = pickle.load(f)
                except EOFError:
                    data = []
                    
            for item in data:
                if old_flight_number in item['Flight Number']: 
                    item['Flight Number'] = flight_number
                    item['Airline Name'] = airline_name,
                    item['Origin'] = origin,
                    item['Destination'] = destination,
                    item['Departure Time'] = departure_time,
                    item['Arrival Time'] = arrival_time
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
            
    
        