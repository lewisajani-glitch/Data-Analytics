monthly_salary = float(input("How much do you earn each month before taxes? $"))

tax_rate = 0.23
tax_withheld = monthly_salary * tax_rate

print(f"The federal tax withheld from a monthly salary of ${monthly_salary:.2f} is\
${tax_withheld:.2f}.")
