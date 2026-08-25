num_for = 0
for n in range(11):
    print(num_for)
    num_for = num_for + 1
num_while = 0
while num_while <= 10:
    print(num_while)
    num_while = num_while + 1

num_for_2 = 10
for n in range(11):
    print(num_for_2)
    num_for_2 = num_for_2 - 1
num_while_2 = 10
while num_while_2 >= 0:
    print(num_while_2)
    num_while_2 = num_while_2 - 1

hash_1 = "#"
while hash_1 != "#######":
    print(hash_1)
    hash_1 = hash_1 + "#"

for row in range(8):
    for column in range(8):
        print("#", end=" ")
    print()

day_10_num = 0
answer = day_10_num * day_10_num
while day_10_num != 11:
    print(f"{day_10_num} x {day_10_num} = {answer}")
    day_10_num = day_10_num + 1
    answer = day_10_num * day_10_num

code_lang = ['Python', 'Numpy','Pandas','Django', 'Flask']
for lang in code_lang:
    print(lang)

for i in range(101):
    if i % 2 == 0:
        print(i)

for i in range(101):
    if i % 2 == 1:
        print(i)

day10_total = 0
for i in range(101):
    day10_total = i + day10_total
print(f"The sum of all numbers is {day10_total}")

day10_total_even = 0
# day10_total_odd = 0
# for i in range(101):
#     if i % 2 == 0:
#         day10_total_even = day10_total_even + i
#     if i % 2 == 1:
#         day10_total_odd = day10_total_odd + i
# print(f"The sum of all evens is {day10_total_even}. And the sum of all odds is {day10_total_odd}")

day10_countries = ['Afghanistan','Albania','Algeria','Andorra','Angola','Antigua and Barbuda','Argentina','Armenia','Australia',
  'Austria','Azerbaijan','Bahamas','Bahrain','Bangladesh','Barbados','Belarus','Belgium','Belize','Benin','Bhutan',
  'Bolivia','Bosnia and Herzegovina','Botswana','Brazil','Brunei','Bulgaria','Burkina Faso','Burundi','Cabo Verde',
  'Cambodia','Cameroon','Canada','Central African Republic','Chad','Chile','China','Colombia','Comoros',
  'Congo, Democratic Republic of the','Congo, Republic of the','Costa Rica',"Côte d'Ivoire",'Croatia','Cuba','Cyprus',
  'Czech Republic','Denmark','Djibouti','Dominica','Dominican Republic','East Timor (Timor-Leste)','Ecuador','Egypt',
  'El Salvador','Equatorial Guinea','Eritrea','Estonia','Eswatini','Ethiopia','Fiji','Finland','France','Gabon','Gambia',
  'Georgia','Germany','Ghana','Greece','Grenada','Guatemala','Guinea','Guinea-Bissau','Guyana','Haiti','Honduras',
  'Hungary','Iceland','India','Indonesia','Iran','Iraq','Ireland','Israel','Italy','Jamaica','Japan','Jordan',
  'Kazakhstan','Kenya','Kiribati','Korea, North','Korea, South','Kuwait','Kyrgyzstan','Laos','Latvia','Lebanon','Lesotho',
  'Liberia','Libya','Liechtenstein','Lithuania','Luxembourg','Madagascar','Malawi','Malaysia','Maldives','Mali','Malta',
  'Marshall Islands','Mauritania','Mauritius','Mexico','Micronesia','Moldova','Monaco','Mongolia','Montenegro',
  'Morocco','Mozambique','Myanmar','Namibia','Nauru','Nepal','Netherlands','New Zealand','Nicaragua','Niger','Nigeria',
  'North Macedonia','Norway','Oman','Pakistan','Palau','Palestine','Panama','Papua New Guinea','Paraguay','Peru',
  'Philippines','Poland','Portugal','Qatar','Romania','Russia','Rwanda','Saint Kitts and Nevis','Saint Lucia',
  'Saint Vincent and the Grenadines','Samoa','San Marino','Sao Tome and Principe','Saudi Arabia','Senegal','Serbia',
  'Seychelles','Sierra Leone','Singapore','Slovakia','Slovenia','Solomon Islands','Somalia','South Africa','South Sudan',
  'Spain','Sri Lanka','Sudan','Suriname','Sweden','Switzerland','Syria','Tajikistan','Tanzania','Thailand','Togo','Tonga',
  'Trinidad and Tobago','Tunisia','Turkey','Turkmenistan','Tuvalu','Uganda','Ukraine','United Arab Emirates',
  'United Kingdom','United States','Uruguay','Uzbekistan','Vanuatu','Vatican City','Venezuela','Vietnam', 'Yemen','Zambia',
  'Zimbabwe']
for country in day10_countries:
    if "land" in country:
        print(country)

day10_fruit = ['banana', 'orange', 'mango', 'lemon']
for reverse in reversed(day10_fruit):
    print(reverse)