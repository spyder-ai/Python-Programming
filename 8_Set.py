# 1. contains distinct items 
# 2. unordered and can add or delete items
# 3. no indexing supported
# 4. supports multitype value

# set1 = {10,20,30,40,50}
# print(set1)

# declaring set using set() constructor
# set2 = set([10,20,30,40,50])
# print(set2)

# empty set is a dictionary
# s3 = {}
# print(type(s3))

# create an empty set
# s4 = set()
# print(type(s4))

# Adding elements to a set
# s = {10,20}
# s.add(30)
# print(s)

# s.add(30) # Ignored because item already exist
# print(s)

# s.update([60,'pro'])
# print(s)

# Removing elements from a set
s = {10,20,30,40}
s.discard(20) # removes items if not exist does nothing
print(s)

s.remove(10) # removes items if not exist raise error
print(s)

s.clear() # clear the set
print(s)

s.add(50) # adding data to the set
print(s)

del s # deleting entire set
# now if we try to print set it will raise and error
