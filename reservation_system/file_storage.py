import pickle
from abc import ABC, abstractmethod

class FileStorage(ABC):

    @abstractmethod
    def read_data(self):
        pass


    @abstractmethod
    def write_data(self, data):
        pass

class FlightFileStorage(FileStorage):
    def __init__(self, filename):
        self.filename = filename

    def read_data(self):
        try:
            with open(self.filename, 'rb') as f:
                flights = pickle.load(f)
        except FileNotFoundError:
            flights = []
        return flights

    def write_data(self, data):
        with open(self.filename, 'wb') as f:
            pickle.dump(data, f)

class SeatFileStorage(FileStorage):
    def __init__(self, filename):
        self.filename = filename

    def read_data(self):
        try:
            with open(self.filename, 'rb') as f:
                seats = pickle.load(f) 
        except FileNotFoundError:
            seats = []
        return seats


    def write_data(self, data):
        with open(self.filename, 'wb') as f:
            pickle.dump(data, f)               

class CustomerFileStorage(FileStorage):
    def __init__(self, filename):
        self.filename = filename

    def read_data(self):
        try:
            with open(self.filename, 'rb') as f:
                customers = pickle.load(f)
        except FileNotFoundError:
            customers = []
        return customers

    def write_data(self, data):
        with open(self.filename, 'wb') as f:
            pickle.dump(data, f)     

class ReservationFleStorage(FileStorage):
    def __init__(self, filename):
        self.filename = filename

    def read_data(self):
        try:
            with open(self.filename, 'rb') as f:
                reservations = pickle.load(f)
        except FileNotFoundError:
            reservations = []
        return reservations

    def write_data(self, data):
        with open(self.filename, 'wb') as f:
            pickle.dump(data, f)            