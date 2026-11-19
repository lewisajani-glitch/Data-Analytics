import random

products = ['Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Webcam',
            'Headset', 'Docking Station', 'USB Hub', 'Desk Lamp', 'Surge Protector']

# Product of the Day
product_of_the_day = random.choice(products)
print(f"Product of the Day: {product_of_the_day}")

# Select 3 products for a usability survey
survey_products = random.sample(products, 3)
print(f"Products selected for survey: {survey_products}")

# Shuffle the products for a presentation
random.shuffle(products)
print(f"Randomized product order: {products}")

# Generate a random transaction count
transaction_count = random.randint(50, 300)
print(f"Daily transaction count: {transaction_count}")