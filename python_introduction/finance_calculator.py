# User input
monthly_income = int(input("Enter your monthly income:  "))
monthly_expenses = int(input("Enter your monthly expenses:  "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses
print("Your monthly savings are $" + str(monthly_savings))

# Calculate annual savings
annual_savings = monthly_savings * 12

# Add 5% interest
interest_rate = 0.05
projected_savings = annual_savings * (1 + interest_rate)

# Print projected savings without decimals
print(f"Projected savings after one year, with interest, is: ${projected_savings:.0f}")
