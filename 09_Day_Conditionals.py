age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    print(f"You need {18 - age} more years to learn to drive")

my_age = 31
your_age = int(input("Enter your age: "))
if my_age >= your_age:
    if my_age == your_age:
        print("You have the same age as me")
    else:
        print(f"I am {my_age - your_age} years older than you")
else:
    print(f"You are {your_age - my_age} years older than me")

user_number_1 = int(input("Enter number one : "))
user_number_2 = int(input("Enter number two: "))
if user_number_1 > user_number_2:
    print(f"{user_number_1} is greater than {user_number_2}")
elif user_number_1 < user_number_2:
    print(f"{user_number_1} is smaller than {user_number_2}")
else:
    print("Your first and second number are both equal to each other")

your_grade = int(input("Enter your marks 0-100: "))
if 90 <= your_grade <= 100:
    print("Your grade is A")
elif 80 <= your_grade <= 89:
    print("Your grade is B")
elif 70 <= your_grade <= 79:
    print("Your grade is C")
elif 60 <= your_grade <= 69:
    print("Your grade is D")
elif your_grade <= 59:
    print("Your grade is F")
else:
    print("Your number was not between 0 and 100")

your_month = input("Enter your month: ").capitalize()
if your_month == "September" or your_month == "October" or your_month == "November":
    print(f"It is Autumn in {your_month}")
elif your_month == "December" or your_month == "January" or your_month == "February":
    print(f"It is Winter in {your_month}")
elif your_month == "March" or your_month == "April" or your_month == "May":
    print(f"It is Spring in {your_month}")
elif your_month == "June" or your_month == "July" or your_month == "August":
    print(f"It is Summer in {your_month}")
else:
    print(f"{your_month} is not a month")

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits)
user_fruit = input("Enter a fruit: ")
user_fruit = user_fruit.lower()
if user_fruit in fruits:
    print("Fruit already exists")
else:
    fruits.append(user_fruit)
    print(fruits)

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
if "skills" in person:
    print(person['skills'][2])
else:
    print("The person has no skills")

if "skills" in person:
    if "Python" in person["skills"]:
        print("This person is good at Python")
    else:
        print("This person has no skills in python")
else:
    print("This person has no skills")

if "skills" in person:
    if "JavaScript" in person['skills'] and "React" in person["skills"]:
        print('He is a front end developer')
    elif "Node" in person['skills'] and "Python" in person['skills'] and "MongoDB" in person["skills"]:
        print('He is a backend developer')
    elif "React" in person['skills'] and "Node" in person['skills'] and "MongoDB" in person['skills']:
        print("He is a fullstack developer")
    else:
        print('unknown title')
else:
    print("This person has no skills")

if "is_married" in person:
    if person["is_married"] is True:
        if "country" in person:
            if person['country'] == "Finland":
                print("Asabeneh Yetayeh lives in Finland. He is married.")
            else:
                print("Asabeneh Yetayeh does not live in Finland. He is married.")
        else:
            print("Asabeneh Yetayeh is married.")
    else:
        print("Asabeneh Yetayeh is not married.")
else:
    print("Unknown if Asabeneh Yetayeh is married.")