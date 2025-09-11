class Order:
    def __init__(self):
        self.items = []
    def add_item(self, item):
        if item.available:
            self.items.append(item)
            print(f"Added {item.name}")
        else:
            print(f"Item is not available.")

    def remove_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                print(f"Removed {item.name}")
                return
        print(f"Item not found in order.")

    def calculate_total(self):
        return sum(item.price for item in self.items)
