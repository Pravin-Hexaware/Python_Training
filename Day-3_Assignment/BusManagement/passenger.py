class Passenger:
    def __init__(self, name, ticket, destination):
        self.name = name
        self.ticket = ticket
        self.destination = destination

    def display(self):
        print(f"{self.name}, Ticket: {self.ticket}, Destination: {self.destination}")