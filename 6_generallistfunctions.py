mine = [1,2,'pro',-1, 22.6, False]
gravel = [22,11,2,34,100,1]

# Min, Max, Sum functions
print(min(mine))
print(max(mine))
print(sum(mine))

# Reversing a list

# 1. Pythonic way
mine.reverse()
print(mine)

# 2. Manual way
# mine2 = []

# a = len(mine) - 1

# while a >= 0:
#     mine2.append(mine[a])
#     a -= 1
# print(mine2)

# sorting a list
gravel.sort()
print(gravel)