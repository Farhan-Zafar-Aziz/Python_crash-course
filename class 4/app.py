#left to right itration is positive indexing
# ->          0          1           2
names = ['sir Qasim','sir Zia','sir Hamzah']
#            -3         -2            -1
#right to left itration is negative indexing

print(names[0]) # sir Qasim
print(names[-3]) # sir Qasim

from typing import Any
# ->                   0           1          2
names: list[Any] = ['sir Qasim','sir Zia','sir Hamzah']
# <-                    -3         -2          -1
print(names[-2]) # sir Zia

# ->                    0           1          2
names: list[Any] = ['sir Qasim','sir Zia','sir Hamzah']
# <-                    -3         -2          -1
print(type(names))
print(type(names[-2]))
print(f'Founder of PIAIC {names[-2].upper()}')
# <class 'list'>
# <class 'str'>
# Founder of PIAIC SIR ZIA

# itration 
# itrative data always work on function type
charactors: list[str] = list("ABCDEFGHIJKLMNOPQRSTUVWXZ")
print(charactors)
# ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Z']

# variable : name[start:end:step]
charactors: list[str] = list("ABCDEFGHIJKLMNOPQRSTUVWXZ")
print(charactors[0:2]) # 0 = include : index 2-1 = 1
# defualt slicing go from left to right
# if you want to slice it from right to left use negative numbers
# always slicing data comes in list type
print(charactors[:2])
print(charactors[ : : ]) # by defualt print all values, in this case assume itself thats why print all given values
print(charactors[-26:-24]) # -26 = include : index -24-1 = -25
print(charactors[0:2:1])
print(charactors[::3]) # every charactor come from sequence after 3rd step
print(charactors[::-1]) # reverse the order of charachters
print(charactors[::-2]) # every second character is selected in reversed order
# ['A', 'B']
# ['A', 'B']
# ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Z']
# ['A']
# ['A', 'B']
# ['A', 'D', 'G', 'J', 'M', 'P', 'S', 'V', 'Z']
# ['Z', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']
# ['Z', 'W', 'U', 'S', 'Q', 'O', 'M', 'K', 'I', 'G', 'E', 'C', 'A']
# ['A']

#                    0    1    2    3    4    5    6    7    8
names: list[str] = ['A', 'D', 'G', 'J', 'M', 'P', 'S', 'V', 'Z']
#                   -9    -8   -7   -6   -5  -4   -3   -2   -1
print(names[1:-3]) # ['V', 'S', 'P']

# List Methods 
names: list[Any] = ['Sir Zia ','Sir Qasim','Sir Imran', 12, True]
print(names)
names[3] = 'Sir Hamzah' # mutable (editable)
print(names)
# ['Sir Zia ', 'Sir Qasim', 'Sir Imran', 12, True]
# ['Sir Zia ', 'Sir Qasim', 'Sir Imran', 'Sir Hamzah', True]

names: list[Any] = ['Sir Zia ','Sir Qasim','Sir Imran', 12, True]
del names[3]
print(names)
# ['Sir Zia ', 'Sir Qasim', 'Sir Imran', True]

n: str = print('Pakistan')
display(n) # this is none-return function
# Pakistan
# None

a: str = id(n) # return function
display(a) 
# 140704755510000

names: list[Any] = ['Sir Zia ','Sir Qasim','Sir Imran', 12, True]
print(names)
print(names.pop())
print(names)
# ['Sir Zia ', 'Sir Qasim', 'Sir Imran', 12, True]
# True
# ['Sir Zia ', 'Sir Qasim', 'Sir Imran', 12]

names: str = []
names.append('sir Zia')
names.append('sir Qasim')
print(names) # ['sir Zia', 'sir Qasim']

names: str = ['a','b','c','d']
names.insert(1,'A') # insert(index,value)
print(names) # ['a', 'A', 'b', 'c', 'd']

names: str = ['Sir Zia ','Sir Qasim','Sir Imran', 12, True]
names.clear()
print(names) # []

a: list[str] = ['A', 'D', 'G', 'J', 'M', 'P', 'S', 'V', 'Z']
b = a.copy() # Deep copy
print(a)
print(b)
b[0] = 'Pakistan'

print(a)
print(b)
# ['A', 'D', 'G', 'J', 'M', 'P', 'S', 'V', 'Z']
# ['A', 'D', 'G', 'J', 'M', 'P', 'S', 'V', 'Z']
# ['A', 'D', 'G', 'J', 'M', 'P', 'S', 'V', 'Z']
# ['Pakistan', 'D', 'G', 'J', 'M', 'P', 'S', 'V', 'Z']

names: list[str] = ['A', 'D', 'G', 'J', 'M', 'A', 'S', 'V', 'Z']

print(names.count('A')) # 2

alpha: list[str] = ['A', 'D', 'G', 'J', 'M', 'P', 'S', 'V', 'Z']
members: list[str] = ['Sir Zia','Sir Inam','Sir Qasim']
# alpha.append(members) # add list as syntax 
alpha.extend(members) # add only list elements
print(alpha) # ['A', 'D', 'G', 'J', 'M', 'P', 'S', 'V', 'Z', 'Sir Zia', 'Sir Inam', 'Sir Qasim']

#                    0    1    2    3    4    5    6    7    8
names: list[str] = ['A', 'D', 'G', 'J', 'M', 'P', 'S', 'V', 'Z']
#                   -9    -8   -7   -6   -5  -4   -3   -2   -1
names.remove('A') # remove with text value
print(names) # ['D', 'G', 'J', 'M', 'P', 'S', 'V', 'Z']

#                    0    1    2    3    4    5    6    7    8
names: list[str] = ['A', 'D', 'G', 'J', 'M', 'P', 'S', 'V', 'Z']
#                   -9    -8   -7   -6   -5  -4   -3   -2   -1
names.index('A') # remove with text value
# 0

#                    0    1    2    3    4    5    6    7    8
names: list[str] = ['A', 'D', 'G', 'J', 'M', 'P', 'S', 'V', 'Z']
#                   -9    -8   -7   -6   -5  -4   -3   -2   -1
names.reverse() # remove with text value
print(names)
# ['Z', 'V', 'S', 'P', 'M', 'J', 'G', 'D', 'A']

#                    0    1    2    3    4    5    6    7    8
names: list[str] = ['Z', 'V', 'S', 'P', 'M', 'J', 'G', 'D', 'A']
#                   -9    -8   -7   -6   -5  -4   -3   -2   -1
names.sort() # remove with text value
print(names) # ['A', 'D', 'G', 'J', 'M', 'P', 'S', 'V', 'Z']

