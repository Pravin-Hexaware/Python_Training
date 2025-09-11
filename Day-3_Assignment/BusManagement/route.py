class Route:
    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end
        
    def display(self):
        print(f"Route: {self.name}, From {self.start} to {self.end}")


