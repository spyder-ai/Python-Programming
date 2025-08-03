# 1. collection of key value pair
# 2. unordered
# 3. unique keys duplicate values allowed
# 4. uses hashing internally

# dict = {110:"xyz", 101:"abc", 105: "bcd", 104: "abc"}
# print(dict)

# printing using for loop
# for key, value in dict.items():
#     print(key, value)

# dict2 = {}
# dict2['Apple'] = 120
# dict2['Orange'] = 150
# dict2['Kiwi'] = 620
# dict2['Mango'] = 300
# dict2[121] = 'Special Coconut'

# print(dict2)

# print(dict2['Mango']) # will return the value associated with the key

# get() function
# get function is the safer side to fetch data, if data doesn't exists it 
# it says None rather throwing an error.

# dict3 = {110:"xyz", 101:"abc", 105: "bcd", 104: "abc"}
# print(dict3.get(101)) # output: is abc
# print(dict3.get(134)) # output: None because item doesn't exist
# print(dict3.get(134, "NA")) # output: NA

# if 134 in dict3:
#     print(dict3[134])
# else:
#     print('NAA')

# Modifying dictionaries
dict4 = {110:"xyz", 101:"abc", 105: "bcd", 104: "abc"}
print(dict4.pop(110)) # output xyz

del dict4[104] # delete key value pair of 104

dict4[200] = 'cde'
print(dict4.popitem()) # output key(200), value(cde) 

print(dict4) # display remaining value i.e, 101 and 105