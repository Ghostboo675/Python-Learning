empty_dog = {}

dog = {'Name': 'Jax' ,
       'Colour': 'Brown' ,
       'Breed': 'Pitbull' ,
       'Legs': '4' ,
       'Age': '7y'}
print(dog)

student_dict = {'First_Name': 'Jake' ,
                'Last_Name': 'Wilson' ,
                'Gender': 'Male' ,
                'Age': '16' ,
                'Marital status': 'Single' ,
                'Skills': ['Basketball' , 'French' , 'Running'] ,
                'Country': 'England' ,
                'City': 'Sheffield' ,
                'Address': "Park"}
print(student_dict)

print(len(student_dict))

print(type(student_dict['Skills']))

student_dict['Skills'].append('Studying')
print(student_dict)

student_key_list = list(student_dict.keys())
print(student_key_list)

student_values_list = list(student_dict.values())
print(student_values_list)

student_items = list(student_dict.items())
print(student_items)

student_dict.pop("City")
print(student_dict)

del student_dict
# Printing creates an error