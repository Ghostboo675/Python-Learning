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


# Day 4 and 5 (Student Grade & Class Manager)

students = ["Jack" , "James" , "Nate" , "Alexa" , "Maria"]
print(f"Students:\n {students}")

grades = [28 , 74 , 85 , 64 , 42]
print(f"\nGrades:\n {grades}")#

number_of_students = len(students)
highest_grade = max(grades)
lowest_grade = min(grades)
average_grade = sum(grades) / len(grades)
grade_range = (max(grades) - min(grades))
print(f"\nNumber of Students: {number_of_students}") # 5
print(f"Highest Grade: {highest_grade}") # 85
print(f"Lowest Grade: {lowest_grade}") # 28
print(f"Average Grade: {average_grade}") # 58.6
print(f"Grade range: {grade_range}") # 57


new_student_project = (input("\nEnter a new student's name: "))
new_student_project = new_student_project.capitalize()
new_student_grade = int(input("Enter their grade: "))

students.append(new_student_project)
grades.append(new_student_grade)

number_of_students = len(students)
highest_grade = max(grades)
lowest_grade = min(grades)
average_grade = sum(grades) / len(grades)
grade_range = (max(grades) - min(grades))

#Students: ["(new_student_project)" , "Jack" , "James" , "Nate" , "Alexa" , "Maria"]  Grade: [(new_student grade) , ]
print("\n")
print(students)
print(grades)
print(f"\nNumber of Students: {number_of_students}")
print(f"Highest Grade: {highest_grade}")
print(f"Lowest Grade: {lowest_grade}")
print(f"Average Grade: {average_grade}")
print(f"Grade range: {grade_range}")

grades.sort()
print(f"\nGrades from lowest to highest: {grades}")
