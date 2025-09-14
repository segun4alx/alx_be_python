monthly_income = int(input("Enter your monthly income:  "))
monthly_expense = int(input("Enter your monthly expenses:  "))
first_result = monthly_income - monthly_expense
print("Your monthly savings are", "$" +str(first_result))
projected_savings = first_result * 12 + (first_result *12 *0.05)
print("Projected savings after one year, with interest, is: $", int(projected_savings))
