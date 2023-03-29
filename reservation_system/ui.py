from flight import Flight

class Client:
    def __init__(self) -> None:
        pass
    
    def main(self):
        print('Enter flight number to check seat availability.')
        flight = Flight()
        flight.list()
    
    def seat_option(self, flight: str):
        pass
    
    def start(self) -> None:
        self.main()
    
    def exit(self) -> None:
        pass

class Staff:
    def __init__(self) -> None:
        self.run = True
    
    def help_text(self) -> None:
        print("\nPress 1 to create flight.")
        print("Press 2 to list flights.")
        print("Press 3 to update a flight record.")
        print("Press 4 to delete a flight record.")
        print("Press q to exit.\n")
    
    def main(self) -> None:
        command = input('Command: ')
        if command == '1':
            self.create_flight()
        elif command == '2':
            self.list_flight()
        elif command == '3':
            self.update_flight()
        elif command == '4':
            self.delete_flight()
        elif command == 'q':
            self.stop()
        else:
            print('Invalid option. Please try again.')
            
        if self.run:
            self.start()
    
    def start(self) -> None:
        self.help_text()
        self.main()
        
    def stop(self) -> None:
        print('\nProgram terminated.')
        self.run = False
        
    def list_flight(self) -> None:
        flight = Flight()
        flight.list()
        
    def create_flight(self) -> None:
        flight_number = input('Enter flight : ')
        airline_name = input('Enter airline name : ')
        origin = input('Enter Origin location : ')
        destination = input('Enter destination : ')
        departure_time = input('Enter departure time (MM-DD-YYYY) : ')
        arrival_time = input('Enter arrival time (MM-DD-YYYY) : ')
        flight = Flight()
        flight.create(flight_number, airline_name, origin, destination, departure_time, arrival_time)
        
    def update_flight(self) -> None:
        old_flight_number = input('Enter a Flight number to update :')
        flight_number = input('Enter Flight Number : ')
        airline_name = input('Enter Airline Name : ')
        origin = input('Enter Origin location : ')
        destination = input('Enter destination : ')
        departure_time = input('Enter departure time (MM-DD-YYYY) : ')
        arrival_time = input('Enter arrival time (MM-DD-YYYY) : ')
        flight = Flight()
        flight.update(old_flight_number, flight_number, airline_name, origin, destination, departure_time, arrival_time)
        
    def delete_flight(self) -> None:
        old_flight_number = input('Enter a Flight number to delete :')
        flight = Flight()
        flight.delete(old_flight_number)

class UI:
    def __init__(self, user_type: str) -> None:
        self.user_type = user_type
    
    def start(self) -> None:
        if self.user_type == 'client':
            client = Client()
            client.start()
        elif self.user_type == 'staff':
            staff = Staff()
            staff.start()
        else:
            raise Exception("User type does not exist.")
    
    def exit(self):
        pass