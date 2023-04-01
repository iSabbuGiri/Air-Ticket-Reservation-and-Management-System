from flight import Flight
from seat import Seat
from reservation import Reservation
from customer import Customer

class Client:
    def __init__(self) -> None:
        self.run = True
               
    def start(self) -> None:
        self.help_text()
        self.flight_main() 

    def help_text(self) -> None:
        print('\n\t\t Welcome to the Flight Reservation System.\n')
        print('Enter 1 for search flights.')
        print('Enter 2 for flight details.')  
        print('Enter q to go back.') 

    def flight_main(self) -> None:
        command = input('Command : ')   
        if command == '1':
            self.search_flight()
        elif command == '2':
            self.flight_detail()
        elif command == 'q':
            self.start()

    def search_flight(self) -> None:
        origin = input('Enter origin : ')
        destination = input('Enter destination : ')
        flight = Flight()
        flight.search(origin, destination)   

    def flight_detail(self) -> None:
        flight_number = input('Enter flight number : ')
        flight = Flight()
        flight.detail(flight_number)         

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
        print('\n\t\t Welcome to the Flight Reservation System.\n')
        print('Enter 1 for Flights.')
        print('Enter 2 for Seats.')
        print('Enter 3 for Customers.')
        print('Enter 4 for Reservations.')
        print('Enter q to quit.')
    
    def main(self) -> None:
        print('\n')
        command = input('Command: ')
        
        if command == '1':
            self.flight_main()   
        elif command == '2':
            self.seat_main()
        elif command == '3':
            self.customer_main()
        elif command == '4':
            self.reservation_main()        
        elif command == 'q':
            self.stop()
        else:
            print('Invalid option. Please try again.')
            
        if self.run:
            self.start()
        
    def flight_main(self) -> None:
        print('\n')
        print('Enter 1 to list flights.')
        print('Enter 2 to create a flight.')
        print('Enter 3 to update a flight.')
        print('Enter 4 to delete a flight.')
        print('Enter 5 to search a flight.')
        print('Enter 6 to view flight details.')
        print('Enter q to go back.')
        
        command = input('\nCommand : ')
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
            
        if self.run:
            self.flight_main()
        
    def list_flight(self) -> None:
        flight = Flight()
        flight.list()   
        
    def flight_detail(self) -> None:
        flight_number = input('Enter flight number : ')
        flight = Flight()
        flight.detail(flight_number)   
          
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

    def reservation_main(self) -> None:
        print('\n')
        print('Enter 1 to list reservation.')
        print('Enter 2 to create a reservation.')
        print('Enter 3 to update a reservation.')
        print('Enter 4 to delete a reservation.')
        print('Enter 5 to search a reservation.')
        print('Enter 6 to view reservation details.')
        print('Enter q to go back.')
        
        command = input('\nCommand : ')
        if command == '1':
            self.list_reservation()
        elif command == '2':
            self.create_reservation()
        elif command == '3':
            self.update_reservation()
        elif command == '4':
            self.delete_reservation()
        elif command == '5':
            self.search_reservation()
        elif command == '6':
            self.reservation_detail()
        elif command == 'q':
            self.start()
            
        if self.run:
            self.reservation_main()
    
    def list_reservation(self) -> None:
        reservation = Reservation()
        reservation.list()
        
    def create_reservation(self) -> None:
        flight_number = input('Enter flight number : ')
        customer_id = input('Enter customer ID : ')
        seat_number = input('Enter seat number : ')
        arrival_date = input('Enter arrival date (MM-DD-YYYY) : ')
        reservation = Reservation()
        reservation.create(flight_number, customer_id, seat_number, arrival_date)
        
    def update_reservation(self) -> None:
        id = input('Enter reservation ID')
        flight_number = input('Enter flight number : ')
        customer_id = input('Enter customer ID : ')
        seat_number = input('Enter seat number : ')
        arrival_date = input('Enter arrival date (MM-DD-YYYY) : ')
        reservation = Reservation()
        reservation.update(id, flight_number, customer_id, seat_number, arrival_date)
        
    def delete_reservation(self) -> None:
        id = input('Enter reservation ID :')
        reservation = Reservation()
        reservation.delete(id) 
    
    def search_reservation(self) -> None:
        customer_name = input('Enter customer name : ')
        reservation = Reservation()
        reservation.search(customer_name)
        
    def reservation_detail(self) -> None:
        id = input('Enter reservation ID : ')
        reservation = Reservation()
        reservation.detail(id)

    def customer_main(self) -> None:
        print('\n')
        print('Enter 1 to list customers.')
        print('Enter 2 to create a customer.')
        print('Enter 3 to update a customer.')
        print('Enter 4 to delete a customer.')
        print('Enter 5 to search a customer.')
        print('Enter q to go back.')
        
        command = input('\nCommand : ')
        if command == '1':
            self.list_customer()
        elif command == '2':
            self.create_customer()
        elif command == '3':
            self.update_customer()
        elif command == '4':
            self.delete_customer()
        elif command == '5':
            self.search_customer()
        elif command == 'q':
            self.start()
            
        if self.run:
            self.customer_main()

    def list_customer(self) -> None:
        customer = Customer()
        customer.list()
        
    def create_customer(self) -> None:
        first_name = input("Enter First Name : ")
        last_name = input("Enter Last Name : ")
        dob = input("Enter Date of Birth (MM-DD-YYYY) : ")
        phone_number = input("Enter Phone Number : ")
        email = input("Enter Email : ")
        customer = Customer()
        customer.create(first_name, last_name, dob, phone_number, email)
        
    def update_customer(self) -> None:
        id = input('Enter customer id : ')
        first_name = input("Enter First Name : ")
        last_name = input("Enter Last Name : ")
        dob = input("Enter Date of Birth (MM-DD-YYYY) : ")
        phone_number = input("Enter Phone Number : ")
        email = input("Enter Email : ")
        customer = Customer()
        customer.update(id, first_name, last_name, dob, phone_number, email)
        
    def delete_customer(self) -> None:
        id = input('Enter customer ID : ')
        customer = Customer()
        customer.delete(id)
    
    def search_customer(self) -> None:
        id = input('Enter customer ID : ')
        customer = Customer()
        customer.search(id)
            
        
    def seat_main(self) -> None:
        print('Enter 1 to create a seat.')
        print('Enter q to exit.')
        
        command = input('Command : ')
        if command == '1':
            self.create_seat()
        elif command == 'q':
            self.stop()
            
        if self.run:
            self.start()
        
    def list_seats(self) -> None:
        seat = Seat()
        seat.list()   
          
    def create_seat(self) -> None:
        flight_number = input('Enter flight : ')
        seat_name = input('Enter seat : ')
        seat_type = input('Enter seat type : ')
        seat = Seat()
        seat.create(flight_number, seat_name, seat_type)

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