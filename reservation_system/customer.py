class Customer:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def get_customer_info(self):
        return f"{self.name}, email: {self.email}, phone: {self.phone}"    