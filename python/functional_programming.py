from functools import reduce

# lambda params: expr(params)

map((lambda x: x ** 2), [1, 2, 3])
map((lambda x: x ** 2), range(10))

# using filter with lambdas
print(list(filter((lambda pair: pair[1] > 0), [(4, 1), (3, 0), (10, 1)])))  # [(4, 1), (10, 1)]

f = lambda a, b: a + b
print(reduce(f, range(1, 201)))


def multiplication(n):
    return n * 2


print(list(map(multiplication, range(1, 10))))
print(list(map(lambda n: n * 2, range(1, 10))))


def times_two(a): return a * 2


def times_three(a): return a * 3


numbers = [1, 2, 3, 4]

both_functions = [times_two, times_three]

print(list(map(lambda num: list(map(lambda a: a(num), both_functions)), numbers)))

countries = ['Switzerland', 'Germany', 'France', 'Austria', 'Italy']

print(list(map(lambda country: len(country), countries)))
print(list(map(len, countries)))

# filter to find the intersections of two lists.
numbers = [-1, 0, 1, 2, 3, 4, 5]
numbers2 = [0, 4, 5, 12, 6, 7, 8]
print(list(filter(lambda a: a in numbers, numbers2)))  # [0, 4, 5]

# 1. map

# Create a list called ``numbers_filter`` of a minimum 5 numbers.
numbers_filter = [4, 6, 9, 10, 23]
# Using ``map`` and ``lambda``, add 10 to each number.
print(list(map(lambda num: num + 10, numbers_filter)))
# Create a list of cities called ``cities_len`` and add a minimum of 5 cities to the list.
favorite_cities = ['New York', 'Paris', 'Moscow', 'Dubai', 'Tokyo']
# Using ``map`` get the length of each city in the list.
print(list(map(len, favorite_cities)))

# 2. filter

# Create a list called ``numbers_filter`` of a minimum 5 numbers.

# Using ``filter`` and ``lambda``, filter out all numbers that are not even.
print(list(filter(lambda num: num % 2 == 0, numbers_filter)))

# 3. reduce

# Import ``reduce`` from ``functools``.

# Create a list called ``numbers_reduce`` of a minimum 5 numbers.
numbers_reduce = [4, 6, 9, 10, 23]
# Using ``reduce`` and ``lambda`` print the sum of the ``numbers_reduce`` list.
print(reduce((lambda a, b: a + b), numbers_reduce))


def greater_then_six(value):
    return value > 6


print(list(filter(greater_then_six, numbers_reduce)))
