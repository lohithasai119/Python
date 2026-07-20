'''
Ploymorphism
------------
->Polymorphism means from
->it allows same method,functions or operator to perform
different tasks depending on the same object...

Types
-----
1.Method Overloading
2.Method Overriding
3.Operator Overloading


1.Method Overloading
--------------------
Method Overloading means having multiple methods with the same
name but different parameters...

ex:
class cal:
    def add(self,num,num_2=0):
        print(num+num_2)
obj = cal()
obj.add(4,7)
        
ex:
class cal:
    def add(self,num,num_2=0):
        print(num+num_2)
    def add(self,num,num_2=0,num_3=7):
        print(num+num_2+num_3)    
obj = cal()
obj.add(45,7)

2.Method Overriding
-------------------
->The Method Overriding occurs when a child class provides its own
implementation of a method already defined in its parent class....

ex:
class animal:
    def sound(self):
        print('Animals make sounds')
class dog(animal):
    def sound(self):
        print('Dog barks')

d = dog()
d.sound()


3.Operator Overloading
----------------------
->This Operator Overloading allows operators (+,-,*) to work differently
for user defined onjects...

i)__add__(+)
ii)__sub__(-)
iii)__mul__(*)
iv)__truediv__(/)
v)__eq__() (==)
vi)__it__() (<)


ex:
class student:
    def __init__(self,marks):
        self.marks = marks
    def __add__(self,other):
        return self.marks - other.marks

s1 = student(56)
s2 = student(67)
print(s1 + s2)

Data Abstraction
----------------
->Data abstraction is the process of hiding implementation
details and showing only the essential data to user...

ex:
-->ATM,car,App

ex:
from abc import ABC, abstractmethod
class parent:

    @abstractmethod
    def display(self):
        pass

ex:
from abc import ABC, abstractmethod
class bank:
    @abstractmethod
    def interest(self):
        raise NotImplementedError('Subclass must implement interest()')

class SBI(bank):
    def interest(self):
        print('SBI interest Rate:6.56%')

class HDFC(bank):
    def interest(self):
        print('HDFC interest Rate:5.5%')

class ICICI(bank):
    def interest(self):
        print('ICICI interest Rate:6.9%')

banks = [SBI(),HDFC(),ICICI()]


for j in banks:
    j.interest()

'''

                                                 
