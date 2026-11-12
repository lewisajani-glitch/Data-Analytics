print("Hello, World!")

message = "Hello, World!"
print(message)

# Hello world prints twice because both fuctions use the same string variable "message" to print the same output. 
# The first fuction print it directly, while the second function prints the value stored in the variable "message".


dollar = 3
cents = 0.50

print(dollar + cents)  # This will print the total amount in dollars, which is 3.5

cents = cents + 0.25  # Adding 25 cents to the existing cents value
print(dollar + cents)  # This will print the new total amount in dollars, which is 3.75

d_str = '3 dollars'
c_str = '50 cents' 
print(d_str + ' ' + c_str)  # This will print the string concatenation of d_str and c_str, resulting in "3 dollars and 50 cents"