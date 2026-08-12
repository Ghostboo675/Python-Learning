tuple_day_6 = ()

bros_names = ("Josh" , "Zack" , "Jake" , "Marcel")
sises_names = ("Leonie" , "Samantha" , "Sarah" , "Alexa")
print(bros_names)
print(sises_names)

siblings = bros_names + sises_names
print(siblings)

print(len(siblings))

siblings = list(siblings)
siblings.append("Mother")
siblings.append("Father")
family_members = tuple(siblings)
print(family_members)

family_members = list(family_members)
parents = tuple(family_members[-2:])
family_members.remove("Mother")
family_members.remove("Father")
siblings = tuple(family_members)
print(parents)
print(siblings)

fruits = ("Apple" , "Pear" , "Orange")
vegetables = ("Carrot" , "Potato" , "Sweetcorn")
animal_products = ("Toy" , "Bed" , "Collar")
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

food_stuff_It = list(food_stuff_tp)
print(food_stuff_It)

print(food_stuff_It[4])

print(food_stuff_It[0:3])
print(food_stuff_It[-3:])

del food_stuff_It
del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)