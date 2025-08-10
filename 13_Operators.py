# Exponentiation (**)
print(2 ** 3) # 8  note Integer * Integer = Integer
print(2 ** 3.) #8.0  Integer * Float  =  FLoat
print(2. ** 3) #8.0  FLoat * Integer = FLoat
print(2. ** 3.) #8.0

# Multipliciation (*)
print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)

# Division (/returns float always)
print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)
# though it always returns a float value, it might create a problem cause sometimes we
# don't exactly need float values rather Integer values this is how we can solve that.

# Integer Division(//floot division)
print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)
# if there is any integer it will remove the fractional part, that's its speciality

'''
    floor division gives the nearest integer value, let me explain how!
    6 / 4 is 1.5, floor will give the floor value of 1.5 i.e, 1
    11 / 4 is 2.75, floor will give the floor value of 2.75 i.e, 2
    -6 / 4 is -1.25, floor will give the floor value of -1.25 i.e, 2
'''
# the floor value of -1.25 is 2 but how?
''' remember the number line '''
# -2.75...-2.45...-2.15...-2...-1.75...-1.45...-1.15...1...1.15...1.45...1.75...2...2.15...2.45...2.75
# so, 1.45 is higher but floor means lowest that is 1
# similarly, -1.45 is higher floor mean lowest that is -2

# Remainder (% modulo)
print(5 % 2)
# this is how it works
'''
    14 // 4 gives 3 → this is the integer quotient;
    3 * 4 gives 12 → as a result of quotient and divisor multiplication;
    14 - 12 gives 2 → this is the remainder.
'''
print(12 % 4.5) # a bit complicated

# Addition (+)
print(1+2)
print(-4. + 8)

# Subtraction (-)
print(-4 - 4)
print(4. - 8)
print(-1.1)
