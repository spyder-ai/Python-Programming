# 1. List can hold multiple values
# 2. we can access list items using indexing
# 3. Negative Indexing is supported
# 4. Ordered and changable

collection = [1,2,3,'Apple', 'Cabbage', 23.6, False]

print(collection[2]) # accessing 3nd element i.e, 3
print(collection[3]) # accessing 4rd element i.e, Apple
print(collection[-1]) # accessing last element i.e, False
print(collection[-2]) # accessing second last element i.e, 23.6

# operations in List
# 1.append
collection.append(99) # append 99 in the list at the end
print(collection)

# 2.insert
collection.insert(2,'Banana') # insert Banana at index 3
print(collection)

# 3.index
print(collection.index('Apple')) # fetch the index of Apple in the list

# 4.remove
collection.remove(3) # remove the item available at index 4
print(collection)

# 5.pop
print(collection.pop()) # pops the last item from the list and print

# 6.pop(index)
print(collection.pop(3)) # pops the value at given index 4 and print
print(collection)

# 7.del
del collection[4] # delete the item available at exact index 4 start from 0 and don't print
print(collection)

# checking items if available in list
print(False in collection) # True because item is available in the list
print('Mango' in collection) # False because item is not available in the list
