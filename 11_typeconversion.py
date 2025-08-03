# we have two types of type conversion
# 1. Implicit type conversion
# a = 10
# b = 2.3
# c = a+b

# print(c) # prints value in floating point

# d = True
# e = a+d # here True means 1, false means 0
# print(e) # we'll get 10 + 1 = 11

# 2. Explicit type conversion
a = '123'
b = 10

c = int(a) + b # string has been converted to integer
print(c) # prints 123 + 10 = 133

# we can perform same operations with list, tuple, set