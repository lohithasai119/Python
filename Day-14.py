'''
Modules
-------
---> A module is a python file(.py) that contains reusable code..

1.varaibles
2.functions
3.classes
4.objects
5.statements

Why this module
---------------
--> Instead of Writing the same code repeadly, we can store it in a
module and use it whenever needed...

Types of modules
----------------
1.User-define
2.Built-in

1.user-define
-----------
ex:
import first_module
print(first_module.add(34,4))

from first_module import add,sub
print(sub(34,4))

import first_module as m
print(m.sub(34,4))

import first_module
print(first_module.add(34,4))
print(first_module.sub(34,4))
print(first_module.mul(4,4))
print(first_module.div(2,25))
print(first_module.mod(2,25))
print(first_module.pow(2,3))
print(first_module.mul(2.5,2.5))


2.Built-in
----------

i)Math
->sqrt()--square root
->factorial()--factorial
->pow() -- power
->ceil() -- rounup
->pi -- pi value
ex:
import math
print(math.sqrt(25))
print(math.factorial(5))
print(math.pow(2,5))
print(math.pi)

from math import *
print(sqrt(25))
print(factorial(5))
print(pow(2,5))
print(pi)

ii)OS
---> The OS module is used to interact with operating system
->getcwd() is get current directory
->mkdir() is new folder
->rmdir() is delete that folder 
ex:
import os
print(os.getcwd())

import os
os.mkdir("USK")

import os
os.rmdir("USK")

import os
os.rename("USK","LOHI")


iii)sys
---> This will provide the information about python interpreter
ex:
import sys
print(sys.version)


iv)random
--> Used to generate random values 
ex:
import random
print(random.randint(1000,9999))

import random
print(random.randint(1000,9999))

colors = ['red','blue','green','pink','yellow']
print(random.choice(colors))



'''

from math import *
print(sqrt(25))
print(factorial(5))
print(pow(2,5))
print(pi)









