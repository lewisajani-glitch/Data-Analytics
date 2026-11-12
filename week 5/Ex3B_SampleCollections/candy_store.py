# Description: This script practices tuples and sets by creating candy-and-flavor combinations.
# Author: Ajani Lewis

# Tuples store ordered collections of items. They cannot be changed after creation.
candy_types = ("Gummy Bears", "Lollipops", "Jelly Beans")
fruity_flavors = ("Mango", "Watermelon", "Blue Raspberry")

# A set stores unique items. Combine tuple items using their index positions.
candy_combinations = {
    f"{candy_types[0]} - {fruity_flavors[0]}",
    f"{candy_types[0]} - {fruity_flavors[1]}",
    f"{candy_types[0]} - {fruity_flavors[2]}",
    f"{candy_types[1]} - {fruity_flavors[0]}",
    f"{candy_types[1]} - {fruity_flavors[1]}",
    f"{candy_types[1]} - {fruity_flavors[2]}",
    f"{candy_types[2]} - {fruity_flavors[0]}",
    f"{candy_types[2]} - {fruity_flavors[1]}",
    f"{candy_types[2]} - {fruity_flavors[2]}"
}

# Print the set three times to observe how its item order behaves.
for attempt in range(1, 4):
    print(f"Today's candy options include (display {attempt}):")
    print(candy_combinations)

# Notes:
# - Tuple indexes start at 0, so candy_types[0] is the first candy type.
# - A set keeps unique values and does not guarantee a particular display order.
# - The order may look the same across repeated prints in one run, but you should
#   not rely on it; it can appear different when the script is run again.
