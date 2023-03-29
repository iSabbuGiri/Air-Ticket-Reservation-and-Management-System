import pandas as pd
import pickle

class Flight:
    # def __init__(self, flight_number, airline_name, origin, destination, departure_time, arrival_time):
    #     self.flight_number = flight_number
    #     self.airline_name = airline_name
    #     self.origin = origin
    #     self.destination = destination
    #     self.departure_time = departure_time
    #     self.arrival_time = arrival_time

    def get_flight_info(self):
        return f"{self.airline_name} {self.flight_number} from {self.origin} to {self.destination} departs at {self.departure_time} and arrives at {self.arrival_time}"
    
    def list(self):
        with open('store/flights.dat', 'rb') as f:
            data = pickle.load(f)
            df = pd.DataFrame(data)
            print(df)
            
    def create(self, flight_number, airline_name):
        with open('store/flights.dat', 'rb') as f:
            # Check if file is empty.
            try:
                data = pickle.load(f)
            except EOFError:
                data = []
                
        data.append(
            {
                'Flight Number': flight_number,
                'Airline Name': airline_name
            }
        )

        with open('store/flights.dat', 'wb') as f:
            pickle.dump(data, f)
            
    def update(self, flight_number, airline_name):
        with open('store/flights.dat', 'rb') as f:
            # Check if file is empty.
            try:
                data = pickle.load(f)
            except EOFError:
                data = []
                
        data.append(
            {
                'Flight Number': flight_number,
                'Airline Name': airline_name
            }
        )

        with open('store/flights.dat', 'wb') as f:
            pickle.dump(data, f)
        