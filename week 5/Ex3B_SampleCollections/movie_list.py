# Description: This script practices creating, sorting, and updating a list of movies.
# Author: Ajani Lewis

# Create a list of favorite movies (or movies to watch).
# These titles are examples; replace them with your own choices if you prefer.
movie_list = [
    "Inception",
    "the Amazing Spider-Man2",
    "Spider-Man: Into the Spider-Verse",
    "Interstellar"
]

# Use len() to count the movies, then print the complete list.
print(f"The list movie_list includes my top {len(movie_list)} favorite movies.")
print(movie_list)

# sorted() displays the items in alphabetical order without changing movie_list.
print("Sorted copy using sorted():")
print(sorted(movie_list))
print("Original list after sorted():")
print(movie_list)

# The .sort() method changes the original list into alphabetical order.
movie_list.sort()
print("Original list after .sort():")
print(movie_list)

# Add another movie to the end of the list using .append().
movie_list.append("The Dark Knight")

# Print the updated description and list.
print(f"The list movie_list includes my top {len(movie_list)} favorite movies.")
print(movie_list)


