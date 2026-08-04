import math

print("Day 2: 30 Days of python programming")

first_name = "Samuel"
print(first_name)

last_name = "Omoruyi"
print(last_name)

full_name = first_name + " " + last_name
print(full_name)

country = "England"
print(country)

city = "Sheffield"
print(city)

age = 16
print(age)

year = 2017
print(year)

is_married = True
print(is_married)

is_true = True
print(is_true)

is_light = False
print(is_light)

best_years = [2017, 2020, 2022, 2025, 2026]
print(best_years)

print(type(first_name))
print(type(last_name))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(best_years))

print(len(first_name))

print(f"The len of {first_name} / first name is: {len(last_name) - len(first_name)} smaller than the last name")

num1 = 5
num2 = 4

total_adding = num1 + num2
print(total_adding)

total_subtracting = num1 - num2
print(total_subtracting)

total_multiplying = num1 * num2
print(total_multiplying)

total_dividing = num1 / num2
print(total_dividing)

total_remain_after_dividing = num2 % num1
print(total_remain_after_dividing)

total_powering = num1 ** num2
print(total_powering)

total_floor_division = num1 // num2
print(total_floor_division)

day2_radius = 30
day2_area_of_a_circle = math.pi * (day2_radius ** 2)
print(day2_area_of_a_circle)
day2_circumference = math.pi * (day2_radius * 2)
print(day2_circumference)

user_first_name = input("Enter your first name: ")
user_last_name = input("Enter your last name: ")
user_country = input("Enter your country: ")
user_age = input("Enter your age: ")
print(f"First name: {user_first_name}, Last name: {user_last_name}, Country: {user_country}, Age: {user_age}")

help('keywords')