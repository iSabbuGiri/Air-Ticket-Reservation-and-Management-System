import pickle

class Customer:
    def validate_customer(self, customer_id: str, data: dict) -> bool:
        """
        Method to check if duplicate customer exists during creation and update.
        Returns boolean value.
        """
        with open('customers.dat', 'rb') as f:
            try:
                data = pickle.load(f)
            except EOFError:
                return True
            else:
                for item in data:
                    if customer_id in item['Customer ID']:
                        return False
            return True
    
    def list(self):
        with open('customers.dat', 'rb') as f:
            data = pickle.load(f)
            for item in data.values():
                print(item)
            
    def create(self, customer_id: str, name: str, email: str, phone_number: str) -> None:
        with open('customers.dat', 'rb') as f:
            try:
                data = pickle.load(f)
            except EOFError:
                data = {}

        if self.validate_customer(customer_id, data):
            customer_data = {
                'Customer ID': customer_id,
                'Name': name,
                'Email': email,
                'Phone Number': phone_number
            }
            
            data[customer_id] = customer_data
            
            with open('customers.dat', 'wb') as f:
                pickle.dump(data, f)
        else:
            print('Customer ID must be unique.')
            
    def update(self, old_customer_id: str, customer_id: str, name: str, email: str, phone_number: str) -> None:
        with open('customers.dat', 'rb') as f:
            try:
                data = pickle.load(f)
            except EOFError:
                data = {}
                    
        if old_customer_id in data and self.validate_customer(customer_id, data):
            customer_data = {
                'Customer ID': customer_id,
                'Name': name,
                'Email': email,
                'Phone Number': phone_number
            }
            
            data[customer_id] = customer_data
            del data[old_customer_id]
            
            with open('customers.dat', 'wb') as f:
                pickle.dump(data, f)
        else:
            print('Customer does not exist or new Customer ID is not unique.')
            
    def delete(self, customer_id: str) -> None:
        with open('customers.dat', 'rb') as f:
            try:
                data = pickle.load(f)
            except EOFError:
                data = {}
                
        if customer_id in data:
            del data[customer_id]
            
            with open('customers.dat', 'wb') as f:
                pickle.dump(data, f)
        else:
            print('Customer does not exist.')
