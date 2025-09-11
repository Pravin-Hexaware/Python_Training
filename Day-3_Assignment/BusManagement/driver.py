class Driver:
    def __init__(self, name, emp_id, license_no):
        self.name = name
        self.emp_id = emp_id
        self.license_no = license_no

    def display(self):
        print(f"Driver: {self.name}, ID: {self.emp_id}, License: {self.license_no}")
