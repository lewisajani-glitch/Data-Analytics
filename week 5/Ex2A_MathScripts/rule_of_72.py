current_savings = 1000
interest_rate = 6

years = 72 / interest_rate
doubled_balance = current_savings * 2

print(f"Your current savings is {current_savings}.")

print(
    f"At a {format(interest_rate / 100, '.0%')} interest rate, "
    f"your savings account will be worth "
    f"{format(doubled_balance, '.2f')} in "
    f"{format(years, '.1f')} years."
)
