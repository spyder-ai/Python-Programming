# A literal is data whose values are determined by the literal itself.
# means..
# integer, float, boolean, complex, string these all are called literals

# Intergers
print('4') # type string
print(4) # type integer

# float
a = 4
b = 4.0
# may be both looks similar but the type is totally different see..
print(type(a))  # interger
print(type(b))  # float

# scientific notations and python
# science -> speed of light 3 X 10^8
        # -> Planck's constant 6.62607 X 10^-34
# pythonic notations
print(f'speed of light{3E8}')
print(f'Planck\'s constant{6.62607E-34}')

''' note the value before E or e could be in decimal not the after one '''

# python may sometimes choose different notations than ours
print(0.000000000000000000000001) # 1e-24
# Python always chooses the more economical form of the number's presentation, and you should take this into consideration when creating literals. 