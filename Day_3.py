import math

age = 16
print(type(age))

height = 5.10
print(type(height))

comp = 2 + 5j
print(type(comp))

# Area of a triangle
base = input("Enter the base of your triangle: ")
base = int(base)
height = input("Enter the height of your triangle: ")
height = int(height)
area_of_triangle = base * height * 0.5
print(round(area_of_triangle))

# Perimeter of a triangle
side_a = input("Enter side a: ")
side_a = int(side_a)
side_b = input("Enter side b: ")
side_b = int(side_b)
side_c = input("Enter side c: ")
side_c = int(side_c)
perimeter_of_a_triangle = side_a + side_b + side_c
print(round(perimeter_of_a_triangle))

# Area and perimeter of a rectangle
width = input("Enter width: ")
width = int(width)
length = input("Enter length: ")
length = int(length)
perimeter_of_a_rectangle = (width * 2) + (length * 2)
print(f"The perimeter of the rectangle is {perimeter_of_a_rectangle}")
area_of_a_rectangle = width * length
print(f"The area of the rectangle is {round(area_of_a_rectangle)}")

# Area and circumference of a circle
radius = input("Enter radius: ")
radius = int(radius)
circumference_of_a_circle = 2 * math.pi * radius
print(f"The circumference of the rectangle is {circumference_of_a_circle}")
area_of_a_circle = math.pi * radius * radius
print(f"The area of the circle is {area_of_a_circle}")

# Skipping to 12 (can't be bother to work it out)

print(len("python"))
print(len("dragon"))
print((len("python")) > len("dragon"))

print(("on" in "python") and ("on" in "dragon"))

print("jargon" in "I hope this course is not full of jargon.")

print(("no" in "python") and ("no" in "dragon"))

length_of_python = len("python")
print(type(length_of_python))
length_of_python = float(length_of_python)
print(type(length_of_python))
length_of_float = str(length_of_python)
print(type(length_of_float))

# How to check if a number is even
print(f" 44 % 2 = {44 % 2} meaning 44 is even because it has 0 remainders so can be divided by 2")
print(f" 33 % 2 = {33 % 2} meaning 33 is odd because it has a remainder of 1 so can't be divided by 2")

day3_floor_answer = 7 // 3
day3_floor_answer = int(day3_floor_answer)
print(day3_floor_answer == 2.7)

print("10" == 10)

print(int(9.8) == 10)

hours = input("Enter hours: ")
hours = int(hours)
rate_per_hour = input("Enter rate per hour: £")
rate_per_hour = int(rate_per_hour)
print(f"Your weekly earning is £{hours * rate_per_hour} ")

number_of_years_lived = input("Enter number of years you have lived: ")
number_of_years_lived = int(number_of_years_lived)
print(f"You have lived for {number_of_years_lived * 31536000} seconds")

print(1, 1, 1, 1, 1)
print(2, 1, 2, 4, 8)
print(3, 1, 3, 9, 27)
print(4, 1, 4, 16, 64)
print(5, 1, 5, 25, 125)