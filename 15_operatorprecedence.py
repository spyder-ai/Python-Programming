# See operator has precedence
'''
   Priority 0 - ()                                    N/A
   Priority 1 - **                                    R-L
   Priority 2 - +, -, ~ (Unary plus, minus, bitwise NOT) R-L
   Priority 3 - *, /, //, %                           L-R
   Priority 4 - +, -                                                                                                                                 L-R
'''

# "If operators have the same precedence, they are evaluated according to their associativity — which is usually L–R,
# but ** is an exception with R–L."
print(2*3%5)

# exception
print(2 ** 2 ** 3) # (2**3)= 8, (2 ** 8)= 256

# Besides **, there are a few other exceptions in Python where Right-to-Left (R–L) associativity is used
# 1.Exponentiation
print(2 ** 2 ** 3)  # → 2 ** (2 ** 3) = 256 ✅

# 2. Assignment Operators (=, +=, -=, etc.)
a = b = c = 5
print(a, b, c)  # Output: 5 5 5

# 3. Lambda Functions
f = lambda x: lambda y: x + y
print(f(2)(3))  # Output: 5

# If operators have different priority levels, Python uses precedence rules,
# NOT associativity. Operators with higher precedence are evaluated first.
print(5 % 2 ** 3)  # 5 % (2 ** 3) → 5 % 8 → 5


# Practice
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2) # 10.0

print((2 ** 4), (2 * 4.), (2 * 4)) # 16,8.0,8

print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4)) # -0.5, 0.5, 0, -1

print((2 % -4), (2 % 4), (2 ** 3 ** 2)) # -2, 2, 512
