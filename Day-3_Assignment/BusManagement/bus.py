from driver import Driver
from passenger import Passenger
from route import Route


class Bus:
    def __init__(self,number,capacity):
        self.number = number
        self.capacity = capacity
        self.driver = None
        self.route = None
        self.__passengers = []

    def assign_driver(self, driver):
        self.driver = driver

    def assign_route(self, route):
        self.route = route

    def add_passenger(self, passenger):
        if len(self.__passengers) < self.capacity:
            self.__passengers.append(passenger)
        else:
            print("Bus is full")

    def remove_passenger(self, name):
        for p in self.__passengers:
            if(name!=p.name):
                self.__passengers.remove(name)



    def start_trip(self):
        print(f"Bus {self.number} | Driver: {self.driver.name} | Route: {self.route.start} → {self.route.end}")
        for p in self.__passengers:
            print(p)

    def end_trip(self):
        self.passengers.clear()
        print("Trip ended. Bus is empty.")

    