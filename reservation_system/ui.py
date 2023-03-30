from flight import Flight
from seat import Seat
from reservation import Reservation

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
        
    def start(self) -> None:
        self.help_text()
        self.main()
        
    def stop(self) -> None:
        print('\nProgram terminated.')
        self.run = False
    
    def help_text(self) -> None:
        print('\n')
        print('Enter 1 for Flights.')
        print('Enter 2 for Seats.')
        print('Enter 3 for Customers.')
        print('Enter 4 for Reservation.')
    
    def main(self) -> None:
        command = input('Command: ')
        
        if command == '1':
            self.flight_main()   
        elif command == '2':
            self.seat_main()
        elif command == 'q':
            self.stop()
        else:
            print('Invalid option. Please try again.')
            
        if self.run:
            self.start()
        
    def flight_main(self) -> None:
        print('Enter 1 to list flights.')
        print('Enter 2 to create a flight.')
        print('Enter 3 to update a flight.')
        print('Enter 4 to delete a flight.')
        print('Enter 5 to search a flight.')
        print('Enter 6 to view flight details.')
        print('Enter q to exit.')
        
        command = input('Command : ')
        if command == '1':
            self.list_flight()
        elif command == '2':
            self.create_flight()
        elif command == '3':
            self.update_flight()
        elif command == '4':
            self.delete_flight()
        elif command == '5':
            self.search_flight()
        elif command == '6':
            self.flight_detail()
        elif command == 'q':
            self.start()
            
        self.flight_main()
        
    def list_flight(self) -> None:
        flight = Flight()
        flight.list()   
        
    def flight_detail(self) -> None:
        flight = Flight()
        flight.detail()   
          
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
        
    def search_flight(self) -> None:
        origin = input('Enter origin : ')
        destination = input('Enter destination : ')
        flight = Flight()
        flight.search(origin, destination)
        
    def seat_main(self) -> None:
        print('Enter 1 to list seats.')
        print('Enter 2 to create a seat.')
        print('Enter q to exit.')
        
        command = input('Command : ')
        if command == '1':
            self.create_seat()
        elif command == 'q':
            self.start()
            
        self.seat_main()
        
    def list_seats(self) -> None:
        seat = Seat()
        seat.list()   
          
    def create_seat(self) -> None:
        flight_number = input('Enter flight : ')
        seat = input('Enter seat : ')
        seat_type = input('Enter seat type : ')
        seat = Seat()
        seat.create(flight_number, seat, seat_type)

    def list_reservations(self) -> None:
        reservation = Reservation()
        reservation.list()
        
    def create_reservation(self) -> None:
        flight_number = input('Enter flight number : ')
        customer_name = input('Enter customer name : ')
        seat_number = input('Enter seat number : ')
        reservation = Reservation()
        reservation.create(flight_number, customer_name, seat_number)
        
    def update_reservation(self) -> None:
        old_reservation = input('Enter a reservation to update (in the format "flight_number-customer_name-seat_number") :')
        flight_number = input('Enter flight number : ')
        customer_name = input('Enter customer name : ')
        seat_number = input('Enter seat number : ')
        reservation = Reservation()
        reservation.update(old_reservation, flight_number, customer_name, seat_number)
        
    def delete_reservation(self) -> None:
        old_reservation = input('Enter a reservation to delete (in the format "flight_number-customer_name-seat_number") :')
        reservation = Reservation()
        reservation.delete(old_reservation) 

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


   