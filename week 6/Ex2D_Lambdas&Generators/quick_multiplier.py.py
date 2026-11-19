
# Exercise 2.D - Lambdas and Generators
# Lab 1 - Quick Multipliers

# Double any value
doubler = lambda n: n * 2

print("Doubler:")
print(doubler(8))
print(doubler(-4))
print(doubler("banana"))

print()


# Triple any value
tripler = lambda n: n * 3

print("Tripler:")
print(tripler(8))
print(tripler(-4))
print(tripler("banana"))

print()


# Create a multiplier function that generates lambda functions
def multiplier(n):
    return lambda x: x * n


# Create multipliers from 4 through 10
quadrupler = multiplier(4)
quintupler = multiplier(5)
sextupler = multiplier(6)
septupler = multiplier(7)
octupler = multiplier(8)
nonupler = multiplier(9)
decupler = multiplier(10)


# Test each multiplier
print("Multipliers from 4 through 10:")
print(quadrupler(3))
print(quintupler(3))
print(sextupler(3))
print(septupler(3))
print(octupler(3))
print(nonupler(3))
print(decupler(3))
