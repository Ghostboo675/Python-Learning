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