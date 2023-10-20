# Arithmetic operators are used with numeric values to perform common mathematical operations:

a: int = 7
b: int = 2

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b)
# 9
# 5
# 14
# 3.5
# 1
# 49
# 3

# Assignment operators are used to assign values to variables:

#assign 
a: int = 7
print(a)
# 7

# +=
a: int = 8
print(a)
a += 12
print(a)
# 8
# 20

# -=
a: int = 10
print(a)
a -= 2
print(a)
# 10
# 8

# *=
a: int = 2 
print(a)
a *= 2 
print(a)
# 2
# 4

# /=
a: int = 10
print(a)
a /= 2
print(a)
# 10
# 5.0

# %=
a: int = 11
print(a)
a %= 2
print(a)
# 11
# 1

# //=
a: int = 15
print(a)
a //= 2
print(a)
# 15
# 7

# Comparison operators are used to compare two values:

# == 
a: int = 7
b: int = 10
print(a == b)

a: int = 7
b: int = 7
print(a == b)

a: int = 7
b: str = '7'
print(a == b)
# False
# True
# False

# <, >
a: int = 6
b: int = 5
print(a > b)

a: int = 5
b: int = 6
print(a < b)
# True
# True

# >=, <=
a: int = 5
b: int = 10
print(a <= b)

a: int = 10
b: int = 5
print(a >= b)

a: int = 5
b: int = 10
print(a >= b)

a: int = 10
b: int = 5
print(a <= b)
# True
# True
# False
# False

a: str = 'A'
b: str = 'B'
print(a >= b)

a: str = 'A'
b: str = 'B'
print(a <= b)
# False
# True

# ASCII Code conversion
chr(65) # A

ord('A') # 65

# and Laazmi 
# or optional
# not invert comparison
print(True and True and True)
print(False and False and True)

print(True or True or True)
print(False or False or True)

not True # False
not False # True

name: str = 'Zia Khan'
print(not name == 'Zia Khan') # this code work in your VS code prompt

# is identity operator
x: str = 'abc'
z: str = 'abc'
# value same h is liye back-end mn inka code same h is liye ans will be True 
# agr variable name same hota or value change hoti to  bhi ans will be True
# agr name change hota or value bhi change hoti to ans will be False
x is z # True due to same value

a: str = 'ab'
a: str = 'cb'
a is a # True due to same variable name

a: str = 'ab'
b: str = 'cb'
a is b # False due to different variable name and different value

names: list[str] = ['sir zia','sir hamza','sir imran']
name: str = input('Enter your name')
name in names 
name not in names # convert 

print(3 + 2 - 2 * 4/2 + 2)
# 3.0