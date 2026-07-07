'''
functions
---------
---> functions is a block of code that can reusable
---> function can avoid the repeated line of code...

funtions are two types
----------------------
1.built-in
ex: print(),max(),int(),type(),min(),sum()...etc
2.user-define
---> this function starts with keyword (def)
syntax: def function_name(parameters):
            ------
            ------
            ------
        function_name(arguments)

ex:def add():
     print("hello")
   add()

Types of aruguments
-------------------
1.Required arguments
--->we have pass same number arguments with definition
of the function...
ex:
def add(a,b):
    print(a)
add(2) #it should not use like this  

2.default
--->
ex:
num = 7
num_2 = 9
num_3 = 5
def add(a,b,c):
    print(a)
    print(b)
    print(c)
add(num,num_2,num_3) 


3.keyword
---> we can pass as a pair like(variable = datatype)
ex:
def add(a,b):
    print(a)
add(a="lohi",b="lilly")
ex:
def add(a,b):
    print(a+b)
add(a=9,b=2) 


4.variable length
--->can pass n number arguments and just use (*args) in the
parameter, will recieve tuple arguments...
ex:for tupels(*args)
num = 7
num_2 = 9
num_3 = 5
num_4 = "python"
def add(*a):
    print(a[1])
add(num,num_2,num_3,num_4) 

ex: for dictionaries(**astrisk)
def all(**any):
    print(any["age"])
all(name = "lohi",age = 15) 

scope of varaibles
------------------
i)global variable-->(outside the function)
ex:
num = 9
def func_():
    print(num)
func()

ii)local varailble-->(inside the function)
ex:
def func_():
    num = 89
    print(num)
func_()
print(num)

**NOTE
To change the global varaible by using keyword(global) that
can changed completly inside and outside of the function..
ex:
num = 9
def func_():
    global num
    num = 89
    print(num)
func_()


passing by value
----------------
ex:
a =(1,2,3)
def some(a):
    for j in a:
        print(j)
some(a)    

return keyword
--------------
---> in a function if a return is executed then it will
Functions.py
ex:
def myfun_(b):
    return 5 + b    
a = myfunc_(10)
c = myfunc_(100)
print(a)
print(c)

recursive function
------------------
---> Recursive function that calls itself repeatedly untill
specified condition is met...
syntax:
def func_name(parameter):
    if condition:--> base case
        return statement
    else:
        return statement
print(func_name(arguments))        

ex:
def func_name(num):
    if num == 1:
        return 1
    else:
        return num * func_name(num -1)
num = 5
print(func_name(num))


'''


def func_name(num):
    if num == 1:
        return 1
    else:
        return num * func_name(num -1)
num = 5
print(func_name(num))   









    
