
# Exercise 2.C - Creating and Calling Functions
# Lab 2 - More Functions


# Function 1: Display a mailing label
def display_mailing_label(name, address, city, state, zip):
    print(name)
    print(address)
    print(f"{city}, {state} {zip}")
    print()


# Test mailing labels with two different people
display_mailing_label("Ajani Lewis", "123 Main Street", "Philadelphia", "PA", "19101")

display_mailing_label("John Smith", "456 Oak Avenue", "New York", "NY", "10001")


# Function 2: Add numbers
def add_numbers(*args):
    total = sum(args)
    equation = " + ".join(str(number) for number in args)
    print(f"{equation} = {total}")


# Test adding numbers
add_numbers(5)
add_numbers(10, 20)
add_numbers(5, 10, 15, 20, 25)


# Function 3: Display receipt and calculate change
def display_receipt(total_due, amount_paid):
    print(f"Total Due: ${total_due:.2f}")
    print(f"Amount Paid: ${amount_paid:.2f}")

    if amount_paid >= total_due:
        change = amount_paid - total_due
        print(f"Change Due: ${change:.2f}")
    else:
        balance = total_due - amount_paid
        print(f"Remaining Balance: ${balance:.2f}")

    print()


# Test 1: Overpayment
display_receipt(45.75, 50.00)

# Test 2: Exact payment
display_receipt(25.00, 25.00)

# Test 3: Underpayment
display_receipt(60.00, 40.00)
