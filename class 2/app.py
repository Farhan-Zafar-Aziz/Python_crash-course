# simple Hello world

print("Hello World!")

# Variables and simple Data types

#Data Types: Python has several built-in data types, including:
#Integers (int): Used to represent whole numbers. For example:
age: int = 18

#Floating-Point Numbers (float): Used to represent real numbers with a decimal point. For example:
pi: float = 3.141592653589793

#Boolean (bool): Represents either True or False. Typically used for conditional statements and logical operations. For example:
is_student: bool = True

#Lists (list): Ordered, mutable collections of items. Lists can contain elements of different data types. For example:
fruits: list = ["apples","mangoes","grapes"]

#Tuples (tuple): Ordered, immutable collections of items. Like lists, but their elements cannot be changed after creation. For example:
my_tuple: tuple = ("apple", "banana", "cherry")

#Strings (str): Used to represent text. Strings are enclosed in either single (') or double (") quotes. For example:
name: str = "Quaid e Azam"

#String data type in python

#boundries
# 'string text', "string text", '''string text''', """string text"""
name: str = "Farhan Aziz"
print(type(name))
print(name)
#<class 'str'>
#Farhan Aziz

#convert any special charactor into simple charactor, place \ before charactor
message: str = 'Piaic "student" card\n father\'s Name'
print(message)
massage: str = "piac 'student' card\n father's Name"
print(massage)
#Piaic "student" card
#father's Name
#piac 'student' card
#father's Name

name: str = "Farhan Aziz"
father_name: str = "Zafar Aziz"
education: str = "Software Engineer"
age: int = 18
city: str = "Karachi"

card: str = "PIAIC Student Card\nStudent Name:"+ name + "\nFather_name:" + father_name + "\nEducation:" + education + "\nAge:" + str(age) + "\nCity:" + city
#age variable is intiger thats why we convert it into string using "str()" function  called as type casting

#print(card)
#PIAIC Student Card
#Student Name:Farhan Aziz
#Father_name:Zafar Aziz
#Education:Software Engineer
#Age:18
#City:Karachi

#\\ back slash use for line continue
print(2 + \
    2 + \
        3)

#Define Multiline string
name: str = "Farhan Aziz"
father_name: str = "Zafar Aziz"
education: str = "Software Engineer"
age: int = 18
city: str = "Karachi"

card: str = """
PIAIC Student Card
Name: 
Father's Name: 
Education:
Age:
City:

"""
print(card) 
# PIAIC Student Card
# Name: 
# Father's Name: 
# Education:
# Age:
# City:       

#f-string power
name: str = "Farhan Aziz"
father_name: str = "Zafar Aziz"
education: str = "Software Engineer"
age: int = 18
city: str = "Karachi"

card: str = f"""
PIAIC Student Card
Name: {name}
Father's Name: {father_name}
Education: {education}
Age: {age}
City: {city}

Total: {2 + 3 + 4}
"""
print(card)
# PIAIC Student Card
# Name: Farhan Aziz
# Father's Name: Zafar Aziz
# Education: Software Engineer
# Age: 18
# City: Karachi

#f-string  mostly use this type
f'''
name: {name}
'''

#jinja style
#work with html page in browser and using with 2x curly brackets
"""
name: {{name}}
"""

#this is old way only know don't use it
name: str = "Farhan Aziz"
father_name: str = "Zafar Aziz"
education: str = "Software Engineer"
age: int = 18
city: str = "Karachi"

card: str = f"""
PIAIC Student Card
Name: %s
Father's Name: %s
Education: %s
Age: %d
City: %s


""" %(name,father_name,education,age)
print(card)

#check methods of string type
dir(str)

# some common string methods
naam: str = "farhan aziz"
print(naam.capitalize())
print(naam.lower())
# format method
a = 7
b = 8 
"Pakistan value a = {} and value b = {}".format(a,b)
#'Pakistan value a = 7 and value b = 8'

#wrong sequence
name: str = "Farhan Aziz"
father_name: str = "Zafar Aziz"
education: str = "Software Engineer"
age: int = 18
city: str = "Karachi"

card: str = """
PIAIC Student Card
Name: {}
Father's Name: {}
Education: {}
Age: {}
City: {}


""" .format(father_name,name,education,city,age)
#              1         0       2       4   3
print(card)
# PIAIC Student Card
# Name: Zafar Aziz
# Father's Name: Farhan Aziz
# Education: Software Engineer
# Age: Karachi
# City: 18

#correct sequence
name: str = "Farhan Aziz"
father_name: str = "Zafar Aziz"
education: str = "Software Engineer"
age: int = 18
city: str = "Karachi"

card: str = """
PIAIC Student Card
Name: {1}
Father's Name: {0}
Education: {2}
Age: {4}
City: {3}


""" .format(father_name,name,education,city,age)
#              0          1        2    3    4
print(card)
# PIAIC Student Card
# Name: Farhan Aziz
# Father's Name: Zafar Aziz
# Education: Software Engineer
# Age: 18
# City: Karachi

student_code: str = """ 
print("My name is Farhan Aziz") 
a: int = 9
b: int = 9
print(a + b)

"""
exec(student_code)
# My name is Farhan Aziz
# 18

# Explore string methods and attributes
wether: str = "      Pyarwala Moasam       "
print(wether)
print(wether.lstrip()) # remove left-side whitespace "lstrip()" left-side space removal
print(wether.rstrip()) # remove right-side whitspace  "rstrip()" right-side space removal
print(wether.strip()) # remove all side whitespace  

#using strip() method
#       Pyarwala Moasam       
# Pyarwala Moasam       
#       Pyarwala Moasam
# Pyarwala Moasam

#\n , \t, \b
message: str = "Stay with \t Palestine"
print(message) #  \t using for extra space

message: str = "I stand with\n Palestine"
print(message) #  \n using for new line

message: str = "Allah Protect the\b Muslims of Palestine"
print(message) #  \b using for backspace
# Stay with 	 Palestine
# I stand with
#  Palestine
# Allah Protect th Muslims of Palestine