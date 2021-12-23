x = ['Python', 'programming', 'is', 'awesome!']

# filter() takes an iterable, calls the lambda function on each item,
# and returns the items where the lambda returned True.
''' 
    Note: Calling list() is required because filter() is also an iterable.
    filter() only gives you the values as you loop over them.
    list() forces all the items into memory at once instead of having to use a loop.
'''
print(list(filter(lambda val: len(val) > 8, x)))

print(list(map(lambda val: val.upper(), x)))
