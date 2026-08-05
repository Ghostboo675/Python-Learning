# Day 2 and 3 (Personal Finance Calculator)

name = input("Enter your name: ")
monthly_income = input("Enter your monthly income: ")
monthly_rent = input("Enter your monthly rent: ")
monthly_food_expenses = input("Enter your monthly food expenses: ")
monthly_transport_expenses = input("Enter your monthly transport expenses: ")
monthly_entertainment_expenses =input("Enter your monthly entertainment expenses: ")
print("---------------------------------------------------------------------------------------------------")

print(f"Name: {name}")
print(f"Monthly income: {monthly_income}")
monthly_income = float(monthly_income)
print(f"Rent: {monthly_rent}")
monthly_rent = float(monthly_rent)
print(f"Food: {monthly_food_expenses}")
monthly_food_expenses = float(monthly_food_expenses)
print(f"Transport: {monthly_transport_expenses}")
monthly_transport_expenses = float(monthly_transport_expenses)
print(f"Entertainment: {monthly_entertainment_expenses}")
monthly_entertainment_expenses = float(monthly_entertainment_expenses)
print("---------------------------------------------------------------------------------------------------")

total_expenses = monthly_entertainment_expenses + monthly_transport_expenses + monthly_food_expenses + monthly_rent
money_remaining = monthly_income - total_expenses
percent_remaining = round((total_expenses / monthly_income) * 100, 2)
percent_spent = round(100 - percent_remaining, 2)
average_expense = round(total_expenses / 4 , 2)

print(f"Total expenses: {total_expenses}")
print(f"Money remaining: {money_remaining}")
print(f"Percent remaining: %{percent_remaining}")
print(f"Percent spent: %{percent_spent}")
print(f"Average expense: £{average_expense}")
