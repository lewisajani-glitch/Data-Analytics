# Exercise 3.B - More Fun with Classes

class Restaurant:
    """A class that represents a restaurant."""

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0
        self.customer_ratings = []

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")

    def add_num_served(self):
        amount = int(input("How many customers served today? "))
        self.number_served += amount

    def print_num_served(self):
        print(f"{self.rest_name} has served {self.number_served} customers.")

    def customer_rating(self):
        while True:
            try:
                rating = int(input("Rate your experience from 1-5: "))

                if 1 <= rating <= 5:
                    self.customer_ratings.append(rating)
                    average = sum(self.customer_ratings) / len(self.customer_ratings)

                    print(f"Your rating was {rating}. "
                          f"The average rating for this restaurant is {average:.2f}")
                    break
                else:
                    print("Please enter a rating between 1 and 5.")

            except ValueError:
                print("Invalid input. Enter a whole number from 1 to 5.")


restaurant1 = Restaurant("McDonald's", "fast food")
restaurant2 = Restaurant("Olive Garden", "Italian food")
restaurant3 = Restaurant("Sushi Palace", "Japanese food")

print("--- McDonald's ---")
restaurant1.print_num_served()
restaurant1.add_num_served()
restaurant1.add_num_served()
restaurant1.print_num_served()

restaurant1.customer_rating()
restaurant1.customer_rating()
restaurant1.customer_rating()

print("\n--- Olive Garden ---")
restaurant2.print_num_served()
restaurant2.add_num_served()
restaurant2.add_num_served()
restaurant2.print_num_served()

restaurant2.customer_rating()
restaurant2.customer_rating()

print("\n--- Sushi Palace ---")
restaurant3.print_num_served()
restaurant3.add_num_served()
restaurant3.print_num_served()
restaurant3.print_num_served()
restaurant3.print_num_served()
restaurant3.print_num_served()
restaurant3.print_num_served()
restaurant3.print_num_served()
restaurant3.print_num_served()
restaurant3.print_num_served()
restaurant3.print_num_served()
restaurant3.add_num_served()
restaurant3.print_num_served()

restaurant3.customer_rating()
restaurant3.customer_rating()
restaurant3.customer_rating()