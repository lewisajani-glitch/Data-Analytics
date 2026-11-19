# Exercise 3.A - Working with Classes

class Restaurant:
    """A class that represents a restaurant."""

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")


restaurant1 = Restaurant("McDonald's", "fast food")
restaurant2 = Restaurant("Olive Garden", "Italian food")
restaurant3 = Restaurant("Sushi Palace", "Japanese food")

restaurant1.describe_rest()
restaurant1.rest_open()

print()

restaurant2.describe_rest()
restaurant2.rest_open()

print()

restaurant3.describe_rest()
restaurant3.rest_open()