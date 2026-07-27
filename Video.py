#   /// = know it          // = I'll be fine in it             / = Forgettable
# from ctypes import HRESULT

#                            1: Python tutorial for beginners ///


#print("Hello World")
#print("Hello World")
#print("Hello World")

#print(2+5)
#print(2-5)
#print(2/5)
#print(2*5)



#                             2: Variables ///


#name = "Sam"
#print(f"hi {name}")
#age = 15
#print(f"you are {age} years old")



#                             3: Type casting //




#                            4: User input ///

#name = input("What is thy name? " )

#print(f"Hello {name}")
#age = input("What is thy age? ")
#print(f"so {name} is {age} years old")


#                             5: Arithmetric and Math //


#money = 0

#money += 5 # 0 + 5 = 5
#money -= 1 # 5 - 1 = 4
#money /= 2 # 4 / 2 = 2
#money *= 3 # 2 * 3 = 6
#money **= 2 # 6 squared = 36
# write more

#print(money)



#                              6: If statements ///





#                             7: Logical operators ///



#temp = 1
#is_cold = True

#print("THE FIRST EVENT")

#if temp < 0 or is_cold:
#    print("Outside event is closed")
#elif temp > 0 or not is_cold :
#    print("Outside event is open")

#temp2 = 0
#is_sunny = True

#print("THE SECOND EVENT")

#if temp2 > 30 and is_sunny:
#    print("Outside event is hot")
#    print("Outside event is sunny")
#elif temp2 > 0 < 30 and is_sunny:
#    print("Outside event is warm")
#    print("Outside event is sunny")
#elif temp2 < 0 and is_sunny:
#    print("Outside event is cold")
#    print("Outside event is sunny")
#elif temp2 > 30 and not is_sunny:
#    print("Outside event is hot")
#    print("Outside event is cloudy")
#elif temp2 > 0 < 30 and not is_sunny:
#    print("Outside event is warm")
#    print("Outside event is cloudy")
#elif temp2 < 0 and not is_sunny:
#    print("Outside event is cold")
#    print("Outside event is cloudy")
#elif temp2 == 0 and not is_sunny:
#    print("Outside event is warm")
#    print("Outside event is cloudy")
#elif temp2 == 0 and is_sunny:
#    print("Outside event is warm")
#    print("Outside event is sunny")


#                          8: Conditional expressions /

#temperature = 19

#conclusion = "HOT" if temperature > 20 else "COLD"
#print(conclusion)

#House_party = input("Hey, its your friend John. Do you want to go to the house party say yes or no ")
#if House_party.lower() == "yes":
#    temp = input("Ok cool, can you tell me the temperature again? ")
#    temp = int(temp)
#    open = "Nah bro that's way to cold" if temp < 0 else "That's perfect I like it hot"
#    print(open)
#    quit()
#if House_party.lower() == "no":
#    print("Ok bro, guess you don't like me")
#    quit()
#else:
#    print("I don't understand you")


#                         9: String methods ///      25/5/2026

#name1 = input("What is the your name ")
#name1 = len (name1)
#print(name1)

#name2 = input("What is the your name ")
#name2 = name2.find("s")
#print(name2)

#name3 = input("What is the your name ")
#name3 = name3.replace("s", "l")
#print(name3)

#name4 = input("What is the your name ")
#name4 = name4.count("s")
#print(name4)

#name5 = input("What is the your name ")
#name5 = name5.capitalize()
#print(name5)

#name6 = input("What is the your name ")
#name6 = name6.isalpha()
#print(name6)

#print(help(str))


#                            10: String indexing ///            23/06/26


# [Start , End, Step]

# num = "2972-6835-4955-2085"

# print(num[0])
# print(num[1])
# print(num[7])
# print(num[-2])

# print(num[0:4])
# print(num[:8])

# print(num[::2])

# print(f"Your credit card is XXXX-XXXX-XXXX-{num[15:]}")


#                            11.Format specifiers /  25/06/26


# p1 = 2354.97
# p2 = 5395.1987
# p3 = -720

# print(f"p1 is £{p1:+,.2f}")
# print(f"p2 is £{p2:+,.1f}")
# print(f"p3 is £{p3:+,.5f}")

# print(f"p1 is £{p1: >10}")
# print(f"p2 is £{p2: <10}")
# print(f"p3 is £{p3: ^10}")


#                            12. While loops ///  30/06/26


# Num = int(input("Enter a number between 1 and 10: "))

# while Num <= 1 or Num >= 10:
#     print("That is not a valid number.")
#     Num = int(input("Enter a number between 1 and 10: "))

# print(f"Your number is {Num}.")