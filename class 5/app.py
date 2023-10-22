# for loop
names: list[str] = ['sir zia','sir inam','sir imran']

for name in names: # name local variable and names place holder variable
    print(name)
# sir zia
# sir inam
# sir imran

for name in names:
    print(f'''Welcome Dear Teacher {name.title()}''')
# Welcome Dear Teacher Sir Zia
# Welcome Dear Teacher Sir Inam
# Welcome Dear Teacher Sir Imran

for name in names:
    print(f'''Welcome Dear Teacher {name.title()}''')
    print(f'''PIAIC Team Member\n''') # this content will be print with for loop value bcz this msg written in indentation of for loop

print('Pakistan Zinda Bad') # this print out due to indentation of for loop
# Welcome Dear Teacher Sir Zia
# PIAIC Team Member

# Welcome Dear Teacher Sir Inam
# PIAIC Team Member

# Welcome Dear Teacher Sir Imran
# PIAIC Team Member

# Pakistan Zinda Bad

for name in names[ : :-1]: # like that we can pass any value from list
    print(f'''Welcome Dear Teacher {name.title()}''')
    print(f'''PIAIC Team Member\n''')
# Welcome Dear Teacher Sir Imran
# PIAIC Team Member

# Welcome Dear Teacher Sir Inam
# PIAIC Team Member

# Welcome Dear Teacher Sir Zia
# PIAIC Team Member

data_base: list[tuple[str, int]] = [('Sir Zia', 123),('Sir Qasim', 321),('Sir Imran', 456)]

for data in data_base:
    print(data)
# ('Sir Zia', 123)
# ('Sir Qasim', 321)
# ('Sir Imran', 456)

data_base: list[str, str] = [('Sir Zia', '123'),('Sir Qasim', '321'),('Sir Imran', '456')]

enter_user: str = input("Enter User Name")
enter_password: str = input("Enter Password")

data_base: list[tuple[str, int]] = [('Sir Zia', 123),('Sir Qasim', 321),('Sir Imran', 456)]

enter_user: str = input("Enter User Name")
enter_password: str = input("Enter Password")

for data in data_base:
    user, password = (data)
    if enter_user == user and enter_password == password:
        print('Valid user and password')
        break
else: 
    ('Invalid user and password') 
    # when if runs ans will be 'Valid user and password' and when else runs ansr will be 'Invalid user and password'

    name: str = "Farhan"
      print(name) # generate indent error bcz here you can't use as indentation, indentation use when you apply loops or conditions in variable

      name: str = "Farhan"
print(name) # correct syntax

# Numbers in Loop
# range(start,end,step)

range(10) # direct function can't working
# range(0, 10)

list(range(10)) # now it is working
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

list(range(0,21))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

list(range(2,21,2))
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

for i in range(2,21,2):
    print(i)
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20

for n in range(1,11):
    print(f"{2} x {n} = {n*2}")

# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 2 x 4 = 8
# 2 x 5 = 10
# 2 x 6 = 12
# 2 x 7 = 14
# 2 x 8 = 16
# 2 x 9 = 18
# 2 x 10 = 20

for a in range(1,11):
    print(f"{3} x {a} = {a*3}")
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# 3 x 4 = 12
# 3 x 5 = 15
# 3 x 6 = 18
# 3 x 7 = 21
# 3 x 8 = 24
# 3 x 9 = 27
# 3 x 10 = 30

# List Comprehensive 

# for items in item_list:
#        loop_body
        

### comprehensive style

#[loop_body for items in item_list]

# old way
for i in range(1,11):

     print(i**2)
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81
# 100

# latest way in one line
[i**2  for i in range(1,11)] # ok
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

digits: list = [1,2,3,4,5,6,7,8,9,0]
print(max(digits))
print(min(digits))
print(sum(digits))
print(digits)
# 9
# 0
# 45
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# Tuples in Python
# A tuple is a collection data type that is immutable. It can store multiple values of different types and it's ordered, meaning the order

names: tuple[str] = ('A',"B",'C')
print(names[0])
print(names[0:2]) # slicing perform
# A
# ('A', 'B')

names: tuple[str] = ("A",'B',"C")

names[0] = "Pak" # tuple value is not changeable its constant
print(names)

data: tuple[Any] = ('A',[1,2,3],True)

print(data[1])
data[1].append(4)
print(data) # value update in object of in tuple tuple will be same Ok
# [1, 2, 3]
# ('A', [1, 2, 3, 4], True)