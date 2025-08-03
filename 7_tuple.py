# 1. Ordered and unchangable
# 2. supports multitype value
# 3. we can access list items using indexing
# 4. Negative Indexing is supported

my_tuple = (10,20,'pro',10)

# print(my_tuple[0])
# print(my_tuple[-1])

# tuple can be constructed without parentheses
# my_tuple_without_para = 900, 30, 'ban'
# print(my_tuple_without_para)

# Single-item tuple
# single_tuple = (20,)
# print(type(single_tuple))

# Tuple Functions
# 1. length
# print(len(my_tuple)) # 4

# 2. count
# print(my_tuple.count(10)) # 2

# 3. index
# print(my_tuple.index('pro')) # 2

# Slicing Tuples
print(my_tuple[1:3]) # my_tuple[index:literally the position]

# Handling Mixed Data Types
nested_tuple = (10, 'geek', (1, 2, 3))
print(nested_tuple[2])        # Output: (1, 2, 3)
print(nested_tuple[2][1])     # Output: 2