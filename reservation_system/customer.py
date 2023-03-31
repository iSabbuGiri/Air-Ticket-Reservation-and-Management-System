import pickle
import pandas as pd

class Customer:
    def __init__(self) -> None:
        """Default constructor"""
        self.filename = 'store/customers.dat'
    
    def get_data(self) -> tuple[any, bool]:
        """Method to get data from a file and unpickle it."""
        is_empty = False
        data = None
        with open(self.filename, 'rb') as f:
            try:
                data = pickle.load(f)
            except EOFError:
                is_empty = True
                
        return data, is_empty
                
    def get_id(self, first_name: str, last_name: str, dob: str) -> str:
        """Method to create a username from user information."""
        return '{}_{}_{}'.format(first_name, last_name, dob.replace('-', '_'))
    
    def retrieve(self, first_name: str, last_name: str, dob: str, data: dict) -> tuple[dict, bool]:
        """Method to check if customer exists."""
        id = self.get_id(first_name, last_name, dob)
        if id in data:
            return data[id], True 
        return {}, False
    
    def list(self) -> None:
        """Method to list all customers in table like format in the command line interface."""
        data, is_empty = self.get_data()
        if is_empty:
            print('No customer data.')
        else:
            df = pd.DataFrame(data)
            print(df)
    
    def create(self, first_name: str, last_name: str, dob: str, phone_number: str, email: str) -> None:
        """Method to create customer data."""
        go = True
        data, is_empty = self.get_data()
        if not is_empty:
            _, exists = self.retrieve(first_name, last_name, dob, data)
            if exists:
                go = False
        else:
            data = {}
                
        if go:
            payload = {
                    self.get_id(first_name, last_name, dob): {
                    'First Name': first_name,
                    'Last Name': last_name,
                    'Date of Birth': dob,
                    'Phone Number': phone_number,
                    'Email': email
                }   
            }
            
            data.update(payload)
            
            with open (self.filename, 'wb') as f:
                pickle.dump(data, f)
            
    def update(self, id: str, first_name: str, last_name: str, dob: str, phone_number: str, email: str) -> None:
        """Method to update customer data."""
        self.delete(id)
        self.create(first_name, last_name, dob, phone_number, email)
            
    def search(self, id: str) -> dict:
        """Method to search and return customer data."""
        data, is_empty = self.get_data()
        if not is_empty:
            if id in data:
                res = data[id]
                print('\n')
                for key, value in res.items():
                    print('{} : {}'.format(key, value))
            else:
                print('\nCustomer with the given id does not exist.')
        else:
            print('No data.')
    
    def delete(self, id: str) -> None:
        """Delete customer data from id."""
        data, is_empty = self.get_data()
        if not is_empty:
            if id in data:
                del data[id]
                
                with open(self.filename, 'wb') as f:
                    pickle.dump(data, f)
        else:
            print('No data.')