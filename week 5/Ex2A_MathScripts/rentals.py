import math

passengers = int(input("How many people are going on the tour? "))

van_capacity = 15
van_daily_cost = 250
number_of_vans = math.ceil(passengers / van_capacity)
total_van_cost = number_of_vans * van_daily_cost

if passengers > 0:
    cost_per_person = total_van_cost / passengers

    print(f"You need {number_of_vans} vans for {passengers} passengers.")
    print(f"The total van rental cost is ${total_van_cost:.2f}.")
    print(f"The cost per person is ${cost_per_person:.2f}.")
else:
    print("Please enter at least 1 passenger.")
