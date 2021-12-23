# 1. List

# a) Countries
# Create a list in a variable called 'favorite_countries'
favorite_countries = ['USA', 'UK', 'Germany', 'Switzerland', 'India']
print(favorite_countries)
# Select the 4th item in 'favorite_countries'
country = favorite_countries[3]
print(country)
#  Change the 4th item in 'favorite_countries' to ‘Cuba’.
favorite_countries[3] = 'Cuba'
print(favorite_countries)

# b) Cities

# Create a list in a variable called 'favorite_cities'
favorite_cities = ['New York', 'Paris', 'Moscow', 'Dubai', 'Tokyo']
# Select the last item in favorite_cities.
print(favorite_cities[-1])
# Select the 1st to 3rd item in favorite_cities.
print(favorite_cities[:3])

# c) Countries/Cities List of Lists

# Create a list of lists in a variable called list_of_lists with favorite_countries and favorite_cities variables.
list_of_lists = [favorite_countries, favorite_cities]
print(list_of_lists)
# Select the third item in the list of cities.
print(list_of_lists[1][2])
# Select the 3rd to 5th item in the list of countries.
print(list_of_lists[0][3:5])

# d) List Methods

# Get the len() of all the variables created previously.
print(len(favorite_countries))
print(len(favorite_cities))
print(len(list_of_lists))

# In index 1 of favorite_cities, insert() ‘Zürich’.
favorite_cities.insert(1, 'Zürich')
# remove() ‘Zürich’ from index 1.
favorite_cities.remove('Zürich')
# clear() the favorite_countries list.
favorite_countries.clear()
# sort() the favorite_cities list in alphabetical order.
favorite_cities.sort()
# reverse() the favorite_cities list.
favorite_cities.reverse()

# 2. Tuple

# a) Create a tuple called 'my_first_tuple'
my_first_tuple = ('Nitesh', 9623116842, 72.5)
# b) Select your weight.
print(my_first_tuple[2])
# c) Try to change your name to see what happens.
# my_first_tuple[0] = 'Ayush'

# d) Create a tuple called 'my_second_tuple' with the same information, but using tuple packing.
my_second_tuple = 'Nitesh', 9623116842, 72.5
# e) Unpack 'my_second_tuple' using three variable names of your choice and print all three variables.
name, phone, weight = my_second_tuple
print(f'{name} {phone} {weight}')
# f) Get the type() of both variables.
print(type(my_first_tuple))
print(type(my_second_tuple))
# g) Get the len() of both variables.
print(len(my_first_tuple))
print(len(my_second_tuple))

# 3. Dictionaries

# a) Create a dictionary called 'my_first_dictionary' and fill it with three keys.
my_first_dictionary = {'first_name': 'Nitesh', 'telephone': 9623116842, 'weight': 72.5, 'last_name': 'Jawanjal',
                       'cities': favorite_cities}
# b) Add 'last_name' to 'my_first_dictionary'

# c) Create a list of 'favorite cities'  and add it to 'my_first_dictionary' in the key 'cities'
# d) Select the 'cities' key.
print(my_first_dictionary['cities'])
# e) Select the 'cities' key using .get().
print(my_first_dictionary.get('cities'))
# f) Delete the 'cities' key.
del my_first_dictionary['cities']
# g) Get the 'type()' of my_first_dictionary.
print(type(my_first_dictionary))
# h) Get the 'len()' of my_first_dictionary.
print(len(my_first_dictionary))