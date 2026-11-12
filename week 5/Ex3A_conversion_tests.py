# Description: This script tests various numeric
#              conversion techniques
# Author: Sam Q. Newprogrammer

# 1. Define the original variables

a = "  101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5  '

# 2a. Try converting each original variable to an integer.
# Successful conversion:
b_int = int(b)

# The following conversions produce ValueError, so they remain commented out:
# a_int = int(a)  # ValueError: the string contains a decimal point, not a whole number.
# c_int = int(c)  # ValueError: the string contains letters as well as numbers.
# d_int = int(d)  # ValueError: the string contains letters as well as numbers.

# 2b. Try converting each original variable to a float.
# Successful conversions:
a_float = float(a)  # float() accepts the extra spaces around the number.
b_float = float(b)

# The following conversions produce ValueError, so they remain commented out:
# c_float = float(c)  # ValueError: the string contains the word "Stevens".
# d_float = float(d)  # ValueError: the string contains the word "Number".

# 2c. Convert a to a float first, then convert that result to an integer.
a_float_then_int = int(float(a))  # Result is 101; int() removes the decimal part (it does not round).

# 2d. Use slicing to select only the numeric part of each string.
# Python indexes start at 0. The end index is not included in a slice.
a_numeric = float(a[2:7])  # Selects '101.1' and converts it to a float.
b_numeric = int(b[0:2])    # Selects '55' and converts it to an integer.
c_numeric = int(c[0:3])    # Selects '402' and converts it to an integer.
d_numeric = int(d[7:8])    # Selects '5' and converts it to an integer.

# 3. Print each original variable, its value, and its data type.
print("Original variables and types:")
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

# Print each successful conversion, its value, and its data type.
print("\nSuccessful conversions and types:")
print(b_int, type(b_int))
print(a_float, type(a_float))
print(b_float, type(b_float))
print(a_float_then_int, type(a_float_then_int))
print(a_numeric, type(a_numeric))
print(b_numeric, type(b_numeric))
print(c_numeric, type(c_numeric))
print(d_numeric, type(d_numeric))

# 4. Use strip() to remove spaces at the beginning and end of a and d.
# strip() returns a cleaned string; it does not change the original variable.
print("\nStrings after using strip():")
print(a.strip())  # Displays '101.1' without the leading/trailing spaces.
print(d.strip())  # Displays 'Number 5' without the trailing spaces.

# Observations:
# - int() works on strings containing whole-number digits, such as '55'.
# - float() works on strings containing numbers with or without decimals, such as '  101.1 '.
# - int() and float() raise ValueError when the string contains non-numeric words.
# - int(float(a)) works because float() first converts '101.1' into a number.
# - Converting 101.1 to int gives 101 because int() truncates the decimal portion.
# - Slicing selects characters by position; the end index is not included.
# - strip() removes leading and trailing whitespace, but does not remove spaces inside text.
