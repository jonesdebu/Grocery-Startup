class GroceryList:
    def __init__(self):
        """Initialize an empty grocery list"""
        self.groceries = {}

    def get_list(self):
        """Print the current grocery list"""

        print(self.groceries)

    def get_item(self, item):
        try:
            if type(item) != str:
                raise TypeError("item must be a string")
            print(f"You have {self.groceries[item]} {item}")

        except KeyError:
            print(item + " is not in grocery list")

    def add(self, item, num=1):
        """Add a number of item to the list"""

        try:
            if type(item) != str:
                raise TypeError("item must be a string")
            if type(num) != int:
                raise TypeError("number must be an integer")

            self.groceries[item] += num
            print(f"Added: {num} {item}")

        except KeyError:
            self.groceries[item] = num
            print(f"Added: {num} {item}")

    def remove(self, item, num=1):
        """Remove a number of item from the list"""

        try:
            if type(item) != str:
                raise TypeError("item must be a string")
            if type(num) != int:
                raise TypeError("number must be an integer")

            self.groceries[item] -= num
            print(f"Removed: {num} {item}")

        except KeyError:
            print(item + " not in grocery list")
            print(f"Removed: {num} {item}")

    def clear_list(self):
        """Clear the entire grocery list"""

        try:
            del self.groceries
            print("Cleared grocery list")

        except AttributeError:
            print("List was already empty")
            self.groceries = {}
