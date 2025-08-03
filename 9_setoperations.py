# set operations
s1 = {2, 4, 6, 8}
s2 = {3, 6, 9}

print(s1 | s2) # Output: {2, 3, 4, 6, 8, 9} UNION
print(s1 & s2) # Output: {6}                INTERSECTION
print(s1 - s2) # Output: {2, 4, 8}          DIFFERENCE
print(s1 ^ s2) # Output: {2, 3, 4, 8, 9}    SYMMETRIC DIFFERENCE

# UNION
# Combines all unique elements from both sets. 

# INTERSECTION
# Returns only the common elements between the sets. 

# DIFFERENCE
# Returns elements present in the first set but not in the second. 

# SYMMETRIC DIFFERENCE
# Returns elements present in either set but not in both. 

s1 = {2, 4, 6, 8}
s2 = {4, 8}

print(s1.isdisjoint(s2))  # Output: False  ISDISJOINT
print(s1 <= s2)           # Output: False  SUBSET
print(s1 < s2)            # Output: False  PROPER SUBSET
print(s1 >= s2)           # Output: True   SUPERSET
print(s1 > s2)            # Output: True   PROPER SUPERSET

# ISDISJOINT
# Returns True if the two sets have no elements in common.

# SUBSET
# Checks if all elements of the first set are in the second set.

# PROPER SUBSET
# Similar to subset but does not allow both sets to be equal.

# SUPERSET
# Checks if the first set contains all elements of the second set.

# PROPER SUPERSET
#  Similar to superset but does not allow both sets to be equal.