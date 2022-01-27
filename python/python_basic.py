# ternary operator in python
condition = True

x = 1 if condition else 0

print(x)

# we can use _ in big numbers to make counting easy
num = 10_000

# context manger with automatically close resource
with open('../data/NOTICE.txt', 'r') as f:
    file_content = f.read()

# use enumerate when you want an index
x = ['Python', 'programming', 'is', 'awesome!']

for index, lang in enumerate(x, start=1):
    print(index, lang)

# unpacking

# _, if we are not planning to use that variable we can use _ instead
a, _ = (1, 2)
print(a)

# use * if we want to assign rest of the values while unpacking
a, b, *c = (1, 2, 3, 4, 5)
print(c)

a, b, *_ = (1, 2, 3, 4, 5)

# if we want to get last value in d
a, b, *c, d = (1, 2, 3, 4, 5)


