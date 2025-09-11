from bus import Bus
from driver import Driver
from passenger import Passenger
from route import Route

bus = Bus(101, 3)
bus.assign_driver(Driver("John"))
bus.assign_route(Route("egattur", "siruseri"))

bus.add_passenger(Passenger("Amal"))
bus.add_passenger(Passenger("Bobby"))
bus.add_passenger(Passenger("John"))

bus.start_trip()
bus.remove_passenger("Amal")
bus.end_trip()