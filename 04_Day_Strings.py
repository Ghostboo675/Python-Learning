t = "Thirty"
d = "Days"
o = "Of"
p = "Python"
print(f"\'{t}\', \'{d}\', \'{o}\', \'{p}\'")

c = "Coding"
f = "For"
a = "All"
print(f"\'{c}\', \'{f}\', \'{a}\'")

company = '"' + c + " " + f + " " + a + '"'

print(company)

print(len(company))

print(company.upper())

print(company.lower())

print(company.capitalize())
print(company.title())
print(company.swapcase())

print(company[2:16])

print(company.find("Coding"))

print(company.replace("Coding", "Python"))

print("Python for Everyone".replace("Everyone", "All"))

print("Coding For All".split(" "))

print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(","))

print("Coding For All" [0])

print("Coding For All" [-1])

print('"Coding For All"' [10])

name_for_p_acronym = "Python For Everyone"
acronym_p = name_for_p_acronym[0] + name_for_p_acronym[7] + name_for_p_acronym[11]
print(acronym_p)

name_for_c_acronym = "Coding For All"
acronym_c = name_for_c_acronym[0] + name_for_c_acronym[7] + name_for_c_acronym[11]
print(acronym_c)

print("Coding For All". index("C"))

print("Coding For All". index("F"))

print("Coding For All". rfind("l"))

print("You cannot end a sentence with because because because is a conjunction".find("because"))

print("You cannot end a sentence with because because because is a conjunction".rindex("because"))

print("You cannot end a sentence with because because because is a conjunction" [31:54])

print("Coding For All".startswith("Coding"))

print("Coding For All".endswith("coding"))

print("    Coding For All     ".strip())

print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier()) # This is true

libraries = ['Django#', 'Flask#', 'Bottle#', 'Pyramid#', 'Falcon#']
print('# '.join(libraries))

print("I am enjoying this challenge.\nI just wonder what is next")

print("Name \t Age \t Country \t City \nAsabeneh \t 250 \t Finland \t Helsinki")

radius_day_4 = 10
area_day_4 = 3.14 * radius_day_4 ** 2
area_day_4 = int(area_day_4)
print(f"The area of a circle with radius {radius_day_4} is {area_day_4} metres square.")

answer_1_day_4 = 14
answer_2_day_4 = 2
answer_3_day_4 = 48
answer_4_day_4 = 1.33
answer_5_day_4 = 2
answer_6_day_4 = 1
answer_7_day_4 = 262144
print(f"8 + 6 = {answer_1_day_4}\n8 - 6 = {answer_2_day_4}\n8 * 6 = {answer_3_day_4}\n8 / 6 = {answer_4_day_4}\n8 % 6 = {answer_5_day_4}\n8 // 6 = {answer_6_day_4}\n8 ** 6 = {answer_7_day_4}")