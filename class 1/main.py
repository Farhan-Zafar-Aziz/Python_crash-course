print("Hello World")
name = "Zafar Aziz"
print(name)
name = 123 # main.py:4: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
print(name)
print(type(name)) #type
print(id(name))

name: str = 'Zafar Aziz Rajar' # main.py:9: error: Name "name" already defined on line 2  [no-redef]
print(type(name))
pakora: str = 123 # main.py:11: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]

name: str = 34 # main.py:13: error: Name "name" already defined on line 2  [no-redef]
print(name)

# Found 4 errors in 1 file (checked 1 source file)

name: list[str] = ['a','b','c']
name: tuple[str,int,float] = ['a',4,2.5]
name: bool = True
name: any = ['q',3,True]


