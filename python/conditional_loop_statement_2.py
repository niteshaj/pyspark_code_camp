# 1) For loop

# Create a string variable called 'my_iterable_name'. Using a for loop and conditional statements, print all letters
# except vowels (a, e, i, o, u) within your name.
my_iterable_name = 'Nitesh Arun Jawanjal'
for char in my_iterable_name:
    if char not in ['a', 'e', 'i', 'o', 'u']:
        print(char)

# Create a list with your favorite movies called 'my_iterable_movies'. Using a for loop print each one.
my_iterable_movies = ['Avatar', 'Inception', 'Spider Man', 'Joker', 'Avengers']
# Use sorted() on your list and print each one
for movie in sorted(my_iterable_movies):
    print(movie)
# 2) While loop

# Create a 'count' variable with the integer 100. While the 'count' is greater than 10, print the value of the count.
# Don't forget to decrement (-=) the count or you will end up with an endless loop!
count = 100
while count > 10:
    print(count)
    count -= 1

# 3) range()

# Create a for loop using 'range()' from 1 to 200 and print the values.
for val in range(200):
    print(val)

# From the previous loop, change the logic using conditional statements, so if the number can be divided by 3 print
# 'Fizz' or divided by 5 print 'Buzz' rather than the number.
for val in range(200):
    if val % 3 == 0:
        print('Fizz')
    elif val % 5 == 0:
        print('Buzz')

# From the previous loop, change the logic so if the number can be divided by both 3 AND 5 print 'Fizz Buzz',
# rather than the number.
for val in range(1, 200):
    if val % 3 == 0 and val % 5 == 0:
        print(f'Fizz Buzz {val}')

# Play with step within the range and see how your previous answer differs.
for val in range(1, 200, 2):
    if val % 3 == 0 and val % 5 == 0:
        print(f'Fizz Buzz {val}')
# Add reverse() to your range and see what happens.
for val in reversed(range(1, 200)):
    if val % 3 == 0 and val % 5 == 0:
        print(f'{val}')
# 4) Dictionaries

rivers = {
    'Nile': 'Egypt',
    'Amazon': 'Brazil',
    'Rhine': 'Switzerland',
    'Yangtze': 'China',
    'Yellow River': 'China'
}

# Using .keys() loop print all the values river names
for river in rivers.keys():
    print(river)

# Using .values() loop print all the values river countries
for country in rivers.values():
    print(country)

# Using .items() print both river names and countries
for river, country in rivers.items():
    print(f'{river}:{country}')
