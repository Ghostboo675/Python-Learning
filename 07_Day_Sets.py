it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))

it_companies.add("Twitter")
print(it_companies) # 'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon' , 'Twitter'

it_companies.update({"Nvidia" , "OpenAI" , "Anthropic"})
print(it_companies) # 'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon' , 'Twitter' , 'Nvidia' , 'OpenAI' , 'Anthropic'

it_companies.remove("Nvidia")
print(it_companies)

# remove() deletes the word but gives an error if the word was never there
# discard() deletes the word and does nothing if the word was never there

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
A_and_B = A.union(B)
print(A_and_B)

print(A.intersection(B))

print(A.issubset(B))

print(A.isdisjoint(B))

print(A.symmetric_difference(B))

A.update(B)
print(A)
B.update(A)
print(B)

del A
del B
# Printing A or B will give an error

age = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(age))
print(f"List length is: {len(age)}")
age = set(age)
print(type(age))
print(f"Set length is: {len(age)}")

# String: A sequence of characters/text, written inside quotes.
# List: An ordered collection of items that can be changed, added to, or removed from.
# Tuple: is a dataset that can't be changed and can't add new items into its dataset.
# Set: is a dataset that can't be changed but can add new items into its dataset.

#I am a teacher and I love to inspire and teach people.
U_words = set("I am a teacher and I love to inspire and teach people".split())
print(len(U_words))