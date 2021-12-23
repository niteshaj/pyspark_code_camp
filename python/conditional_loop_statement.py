for item in ['Laurent', 'Simon', 'Paul']:
    print(item)

for number in range(1, 200):
    print(number)

for n in range(10):
    if n == 5:
        break
    print(n)

# Iterating over dictionary
person = {'firstname': 'Laurent', 'lastname': 'Hoxhaj', 'age': 26}

for key, value in person.items():
    print(f"Key: {key}, Value: {value}")

for key in person.keys():
    print("Key: ", key)

for value in person.values():
    print("Value: ", value)

# check if a key exists
'firstname' in person.keys()  # => True
'address' in person.keys()  # => False

# check if a value exists
'Laurent' in person.values()  # => True
'Meyer' in person.values()  # => False

# get a list of all keys
keys_list = list(person.keys())  # ['name', 'last_name', 'age']

# ZIP
questions = ['name', 'quest', 'favorite color']
answers = ['Lancelot', 'To seek the holy grail', 'Blue']

# use zip() to generate pairs of entries
for q, a in zip(questions, answers):
    print('What is your {0}? {1}.'.format(q, a))

# Reverse iteration
# use reversed() to loop over sequence in reverse
for i in reversed(range(1, 10, 2)):
    print(i, end=', ')


# Sorted iteration
basket = ['pear', 'banana', 'orange', 'pear', 'apple']

# use sorted to return a new sorted list before iterating
for fruit in sorted(basket):
    print(fruit)


