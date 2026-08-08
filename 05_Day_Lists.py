q_day_5 = []
print(type(q_day_5))

w_day_5 = ["dog" , "cat" , "bird" , "sheep" , "cow" , "horse" , "turtle" ]
print(w_day_5)

print(len(w_day_5))

e_day_5 = w_day_5[0]
r_day_5 = w_day_5[3]
t_day_5 = w_day_5[-1]
print(e_day_5 + " " + r_day_5 + " " + t_day_5)

mixed_data_types = ["Samuel" , 16 , "5:10" , "Single", "sheffield"]
print(type(mixed_data_types))

it_companies = ["Facebook" , "Google" , "Microsoft" , "Apple" , "IBM" , "Oracle" , "Amazon"]
print(type(it_companies))

print(it_companies)

print(len(it_companies))

y_day_5 = it_companies[0]
u_day_5 = it_companies[3]
i_day_5 = it_companies[-1]
print(y_day_5 + " " + u_day_5 + " " + i_day_5)

last_index = len(it_companies) - 1
it_companies[last_index] = "BBC"
print(it_companies)

it_companies.append("Nvidia")
print(it_companies)

it_companies.insert(3, "OpenAI")
print(it_companies)

it_companies[0] = it_companies[0].upper()
print(it_companies)

print("#," .join(it_companies))

is_in_company = "Google" in it_companies
print(is_in_company)

it_companies.sort()
print(it_companies) # ['Apple', 'BBC', 'FACEBOOK', 'Google', 'IBM', 'Microsoft', 'Nvidia', 'OpenAI', 'Oracle']

it_companies.reverse()
print(it_companies) # ['Oracle', 'OpenAI', 'Nvidia', 'Microsoft', 'IBM', 'Google', 'FACEBOOK', 'BBC', 'Apple']

print(it_companies[0:3])

print(it_companies[-3:])

print(it_companies[3:6])

it_companies.pop(0)
print(it_companies)

it_companies.pop(3) and it_companies.pop(3)
print(it_companies)

it_companies.pop() # or pop(-1)
print(it_companies)

it_companies.clear()
print(it_companies)

del it_companies
# print(it_companies) will be an error cause there is no list to print

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
print(front_end + back_end)

full_stack = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']
full_stack.insert(5,'Python')
full_stack.insert(6,'SQL')
print(full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print(ages)
o_day_5 = min(ages)
p_day_5 = max(ages)
print(f"Min: {o_day_5}, Max: {p_day_5}")

ages.append(o_day_5)
ages.append(p_day_5)
print(ages) # [19, 19, 20, 22, 24, 24, 24, 25, 25, 26, 19, 26]

ages.sort() # [19, 19, 19, 20, 22, 24, 24, 24, 25, 25, 26, 26]
median_ages = (24 + 24) / 2
median_ages = int(median_ages)
print(f"Median: {median_ages}")

mean_ages = (19 + 19 + 19 + 20 + 22 + 24 + 24 + 24 + 25 + 25 + 26 + 26) / 12
print(f"Mean: {mean_ages}")

range_ages = (26 -19)
print(f"Range: {range_ages}")

print(abs(o_day_5 - mean_ages) , abs(p_day_5 - mean_ages))

countries = [
  'Afghanistan','Albania','Algeria','Andorra','Angola','Antigua and Barbuda','Argentina',
  'Armenia','Australia','Austria','Azerbaijan','Bahamas','Bahrain','Bangladesh',
  'Barbados','Belarus','Belgium','Belize','Benin','Bhutan','Bolivia',
  'Bosnia and Herzegovina','Botswana','Brazil','Brunei','Bulgaria','Burkina Faso',
  'Burundi','Cabo Verde','Cambodia','Cameroon','Canada','Central African Republic','Chad',
  'Chile','China','Colombia','Comoros','Congo, Democratic Republic of the',
  'Congo, Republic of the','Costa Rica',"Côte d'Ivoire",'Croatia','Cuba','Cyprus',
  'Czech Republic','Denmark','Djibouti','Dominica','Dominican Republic','East Timor (Timor-Leste)',
  'Ecuador','Egypt','El Salvador','Equatorial Guinea','Eritrea','Estonia',
  'Eswatini','Ethiopia','Fiji','Finland','France','Gabon','Gambia','Georgia',
  'Germany','Ghana','Greece','Grenada','Guatemala','Guinea','Guinea-Bissau','Guyana',
  'Haiti','Honduras','Hungary','Iceland','India','Indonesia','Iran','Iraq',
  'Ireland','Israel','Italy','Jamaica','Japan','Jordan','Kazakhstan','Kenya',
  'Kiribati','Korea, North','Korea, South','Kuwait','Kyrgyzstan','Laos','Latvia',
  'Lebanon','Lesotho','Liberia','Libya','Liechtenstein','Lithuania','Luxembourg',
  'Madagascar','Malawi','Malaysia','Maldives','Mali','Malta','Marshall Islands',
  'Mauritania','Mauritius','Mexico','Micronesia','Moldova','Monaco','Mongolia',
  'Montenegro','Morocco','Mozambique','Myanmar','Namibia','Nauru','Nepal',
  'Netherlands','New Zealand','Nicaragua','Niger','Nigeria','North Macedonia','Norway',
  'Oman','Pakistan','Palau','Palestine','Panama','Papua New Guinea','Paraguay',
  'Peru','Philippines','Poland','Portugal','Qatar','Romania','Russia','Rwanda',
  'Saint Kitts and Nevis','Saint Lucia','Saint Vincent and the Grenadines','Samoa',
  'San Marino','Sao Tome and Principe','Saudi Arabia','Senegal','Serbia','Seychelles',
  'Sierra Leone','Singapore','Slovakia','Slovenia','Solomon Islands','Somalia',
  'South Africa','South Sudan','Spain','Sri Lanka','Sudan','Suriname','Sweden',
  'Switzerland','Syria','Tajikistan','Tanzania','Thailand','Togo','Tonga',
  'Trinidad and Tobago','Tunisia','Turkey','Turkmenistan','Tuvalu','Uganda',
  'Ukraine','United Arab Emirates','United Kingdom','United States','Uruguay',
  'Uzbekistan','Vanuatu','Vatican City','Venezuela','Vietnam','Yemen','Zambia','Zimbabwe'
]

print(len(countries)) # 195
print(countries[97])

first_list_countries = countries[0:98]
print(first_list_countries)
second_list_countries = (countries[98:195])
print(second_list_countries)

a_day_5 = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_three_countries = a_day_5[0:3]
print(first_three_countries)
scandic_countries = a_day_5[3:]
print(scandic_countries)