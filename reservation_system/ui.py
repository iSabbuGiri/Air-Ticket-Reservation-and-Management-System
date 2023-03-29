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
        print("Press 1 to create flight.")
        print("Press 2 to list flights.")
        print("Press q to exit.")
    
    def main(self) -> None:
        command = input('Command: ')
        if command == '1':
            self.create_flight()
        elif command == '2':
            self.list_flight()
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
        print('Program terminated.')
        self.run = False
        
    def list_flight(self) -> None:
        flight = Flight()
        flight.list()
        
    def create_flight(self) -> None:
        flight_number = input('Enter Flight Number :')
        airline_name = input('Enter Airline Name :')
        flight = Flight()
        flight.create(flight_number, airline_name)
        
    def update_flight(self) -> None:
        flight_number = input('Enter Flight Number :')
        airline_name = input('Enter Airline Name :')
        flight = Flight()
        flight.update(flight_number, airline_name)

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