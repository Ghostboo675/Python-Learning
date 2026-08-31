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


# Day 6, 7 and 8 (Student Management System)

student_1 = {
    "Name": "Samuel" ,
    "Age": 16 ,
    "Country": "England" ,
    "City": "Sheffield" ,
    "Skills": ['Python' , 'Maths' , 'Physics'] ,
    "Favourite Subject": "Computer Science"
}
print("\nStudent 1\n")
print(f"Name: {student_1["Name"]}")
print(f"Age: {student_1["Age"]}")
print(f"Country: {student_1["Country"]}")
print(f"City: {student_1["City"]}")
print(f"Skills: {student_1["Skills"]}")
print(f"Favourite Subject: {student_1["Favourite Subject"]}")

print("\nUpdated Skills:")
student_1["Skills"].append("Problem Solving")
print(student_1["Skills"])
print(f"Number of skills: {len(student_1["Skills"])}")

student_2 = {
    "Name": "James",
    "Age": 17,
    "Country": "England",
    "City": "Manchester",
    "Skills": ['Python', 'Football', 'Physics'],
    "Favourite Subject": "Physics"
}
print("\nStudent 2\n")
print(f"Name: {student_2["Name"]}")
print(f"Age: {student_2["Age"]}")
print(f"Country: {student_2["Country"]}")
print(f"City: {student_2["City"]}")
print(f"Skills: {student_2["Skills"]}")
print(f"Favourite Subject: {student_2["Favourite Subject"]}")

student_3 = {
    "Name": "Alex",
    "Age": 16,
    "Country": "England",
    "City": "Leeds",
    "Skills": ['JavaScript', 'Maths', 'HTML'],
    "Favourite Subject": "Maths"
}
print(f"\nStudent 3\n")
print(f"Name: {student_3["Name"]}")
print(f"Age: {student_3["Age"]}")
print(f"Country: {student_3["Country"]}")
print(f"City: {student_3["City"]}")
print(f"Skills: {student_3["Skills"]}")
print(f"Favourite Subject: {student_3["Favourite Subject"]}")

print(f"\nAll Students\n")
students = [student_1 , student_2 , student_3]
print(students)

print(f"\nFirst student:")
print(student_1)

print(f"\nFirst student's name:")
print(f"{student_1["Name"]}")

print(f"\nFirst student's skills:")
print(f"{student_1["Skills"]}")

print(f"\nDictionary Information\n")
print("Students 1 keys:")
print(f"{list(student_1.keys())}")

print(f"\nStudent 1 values:")
print(f"{list(student_1.values())}")

print(f"\nStudent 3 after removing City:")
student_3.pop("City")
print(f"{student_3}")

print(f"\nStudent 3 after adding City again:")
student_3["City"] = "Birmingham"
print(student_3)

print(f"\nFinal Information\n")

print(f"Number of students: {len(students)}")

print(f"\nStudent 1: {student_1["Name"]}")
print(f"Student 2: {student_2["Name"]}")
print(f"Student 3: {student_3["Name"]}")


# Day 9 and 10 (Student Quiz Game)

points = 0
pro_name = input("Enter your name: ")
pro_name = pro_name.capitalize()

print(f"\nWelcome {pro_name}!")
print("Answer the following questions.")
print("Each question is worth 1 point.")

print("\nQuestion 1\n")

pro_question_code_lang = input("What programming language are you learning? ")
if pro_question_code_lang.lower() == "python":
    print("Correct!")
    points += 1
else:
    print("Incorrect!")
    print("The correct answer was Python.")

print("\nQuestion 2\n")

pro_question_math = (input("What is 10 + 5? "))
if pro_question_math == "15":
    print("Correct!")
    points += 1
else:
    print("Incorrect!")
    print("The correct answer was 15.")

print("\nQuestion 3\n")

pro_question_symbol = input("What symbol is used to create a comment in Python? ")
if pro_question_symbol == "#":
    print("Correct!")
    points += 1
else:
    print("Incorrect!")
    print("The correct answer was #.")

print("\nQuestion 4\n")

pro_question_loop = input("What keyword is used to create a loop over a list? ")
if pro_question_loop.lower() == "for":
    print("Correct!")
    points += 1
else:
    print("Incorrect!")
    print("The correct answer was for.")

print("\nQuestion 5\n")

pro_question_len = input("What does len() tell you? ")
if pro_question_len.lower() == "length":
    print("Correct!")
    points += 1
else:
    print("Incorrect!")
    print("The answer was length.")

print(f"\nPlayer: {pro_name}")
print(f"Score: {points}/5")
print(f"Percentage: {float(points * 20)}%")
if points == 5:
    print("Excellent! You got everything correct!")
elif points == 4 or points == 3:
    print("Good job! You passed the quiz.")
elif points == 2 or points == 1:
    print("You got some questions correct. Keep practising.")
elif points == 0:
    print("You got 0 correct. Keep learning and try again!")


# Day 1, 2, 3, 4, 5, 6, 7, 8, 9 and 10 (Project: Personal Study Tracker)
# Discontinued
name_pro_10 = input("Enter your name: ")
name_pro_10 = name_pro_10.capitalize()
age_pro_10 = input("Enter your age: ")
country_pro_10 = input("Enter your country: ")
country_pro_10 = country_pro_10.capitalize()
city_pro_10 = input("Enter your city: ")
city_pro_10 = city_pro_10.capitalize()

print(f"\nWelcome {name_pro_10}!\n")

first_subject_pro_10 = input("Enter your first subject: ")
second_subject_pro_10 = input("Enter your second subject: ")
third_subject_pro_10 = input("Enter your third subject: ")
study_time_subject1_pro_10 = float(input(f"How many hours did you study {first_subject_pro_10}? "))
study_time_subject2_pro_10 = float(input(f"How many hours did you study {second_subject_pro_10}? "))
study_time_subject3_pro_10 = float(input(f"How many hours did you study {third_subject_pro_10}? "))

student_pro_10 = {
    "Student": name_pro_10 ,
    "Age": age_pro_10 ,
    "Country": country_pro_10 ,
    "City": city_pro_10 ,
    "Subjects": [first_subject_pro_10, second_subject_pro_10, third_subject_pro_10] ,
    "Subject hours": [study_time_subject1_pro_10, study_time_subject2_pro_10, study_time_subject3_pro_10]
}

print(f"\nStudent: {student_pro_10["Student"]}")
print(f"\nAge: {student_pro_10["Age"]}")
print(f"\nCountry: {student_pro_10["Country"]}")
print(f"\nCity: {student_pro_10["City"]}\n")

print("Subjects:")
print(f"- {student_pro_10["Subjects"][0]}")
print(f"- {student_pro_10["Subjects"][1]}")
print(f"- {student_pro_10["Subjects"][2]}\n")

print("Study hours:")
print(f"{student_pro_10["Subjects"][0]}: {student_pro_10["Subject hours"][0]}")
print(f"{student_pro_10["Subjects"][1]}: {student_pro_10["Subject hours"][1]}")
print(f"{student_pro_10["Subjects"][2]}: {student_pro_10["Subject hours"][2]}\n")

print(f"Total study time: {student_pro_10["Subject hours"][0] + student_pro_10["Subject hours"][1] + student_pro_10["Subject hours"][2]}")
print(f"Average study time: {(float(student_pro_10["Subject hours"][0]) + float(student_pro_10["Subject hours"][1]) + float(student_pro_10["Subject hours"][2])) / 3}")
print(f"Longest session: {max(student_pro_10["Subject hours"])}")
print(f"Shortest session: {min(student_pro_10["Subject hours"])}")
print(f"Study range: {float(max(student_pro_10["Subject hours"])) - float(min(student_pro_10["Subject hours"]))}\n")

print("Subjects:")
print(f"- {first_subject_pro_10}")
print(f"- {second_subject_pro_10}")
print(f"- {third_subject_pro_10}\n")

print("Study days:")
print("- Monday")
print("- Tuesday")
print("- Wednesday\n")

study_time_all_subs_pro_10 = float(study_time_subject1_pro_10) + float(study_time_subject2_pro_10) + float(study_time_subject3_pro_10)
study_level_pro_10 = "nothing"

if study_time_all_subs_pro_10 == 0:
    print("You didn't study today")
    print(f"Study level: Low")
    study_level_pro_10 = "Low"
elif study_time_all_subs_pro_10 >= 1 and study_time_all_subs_pro_10 < 3:
    print("You did some studying, but you could do more.")
    print("Study level: Low")
    study_level_pro_10 = "Low"
elif study_time_all_subs_pro_10 >= 3 and study_time_all_subs_pro_10 > 4:
    print("Good job! You had a productive study session.")
    print("Study level: Medium")
    study_level_pro_10 = "Medium"
elif study_time_all_subs_pro_10 >= 4 and study_time_all_subs_pro_10 > 6:
    print("Excellent! You studied a lot today.")
    print("Study level: Medium")
    study_level_pro_10 = "Medium"
elif study_time_all_subs_pro_10 >= 6:
    print("Excellent! You studied a lot today.")
    print("Study level: High")
    study_level_pro_10 = "High"

print(f"\nStudent: {name_pro_10}")
print(f"Number of subjects: {len(student_pro_10["Subjects"])}")
print(f"Total hours: {student_pro_10["Subject hours"][0] + student_pro_10["Subject hours"][1] + student_pro_10["Subject hours"][2]}")
print(f"Average hours: {(float(student_pro_10["Subject hours"][0]) + float(student_pro_10["Subject hours"][1]) + float(student_pro_10["Subject hours"][2])) / 3}")
print(f"Highest session: {max(student_pro_10["Subject hours"])}")
print(f"Lowest session: {min(student_pro_10["Subject hours"])}")
print(f"Study level: {study_level_pro_10}")

# Weaknesses Right now (Project: Student Study Challenge)

pro_weak_name = input("Enter your name: ")
pro_weak_name = pro_weak_name.capitalize()

pro_weak_subject1 = input("Enter first subject: ")
pro_weak_subject1 = pro_weak_subject1.capitalize()
pro_weak_subject2 = input("Enter second subject: ")
pro_weak_subject2 = pro_weak_subject2.capitalize()
pro_weak_subject3 = input("Enter third subject: ")
pro_weak_subject3 = pro_weak_subject3.capitalize()

pro_weak_subject1_hour = float(input(f"Enter study time (hours) for {pro_weak_subject1}: "))
pro_weak_subject2_hour = float(input(f"Enter study time (hours) for {pro_weak_subject2}: "))
pro_weak_subject3_hour = float(input(f"Enter study time (hours) for {pro_weak_subject3}: "))

pro_weak_dict = {
    pro_weak_subject1: pro_weak_subject1_hour ,
    pro_weak_subject2: pro_weak_subject2_hour ,
    pro_weak_subject3: pro_weak_subject3_hour ,
}

any_sub_pro_weak = ""
while any_sub_pro_weak.lower() != "done":
    any_sub_pro_weak = input("Do you have other subjects: ").capitalize()
    if any_sub_pro_weak.lower() == "done":
        break
    else:
        any_sub_pro_weak_chosen = input(f"Enter study time for {any_sub_pro_weak}: ")

print("\n")
for i in pro_weak_dict:
    print(f"{i}: {pro_weak_dict[i]}")


# 3 weaknesses (Project: Study Session Tracker) (The weaknesses) [while loops][Condition ranges (0–2, 3–5, 6+, etc.)][Nested data (lists/dictionaries inside other data)]
# Discontinued
name_q = input("Enter your name: ")

subject_q = ""
subject_list_q = []
subject_hours_list_q = []

while subject_q.lower() != "done":
    subject_q = input("Enter a subject (or 'done' to finish): ").capitalize()
    if subject_q.lower() == "done":
        break
    else:
        subject_q_hours = float(input("Enter hours studied: "))
        subject_dict_q = {
            "Subjects": subject_q , "Hours": subject_q_hours
        }
        subject_list_q.append(subject_dict_q)

print(subject_list_q)