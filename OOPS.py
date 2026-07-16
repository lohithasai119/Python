'''
OOPs
----
Object-oriented programming system(OOPs),This will be organizes the
code using classes and objects...

Uses
----
-Code reusable
-Easy maintance
-clear understanding
-better security

Classes
-------
class is a blue-print or a template used to create an object...
syntax:
class batch_4:
    pass

Object
------
Object is a instance of the class..
ex:
class student:
    studn = "lohi"
st_ = student()    
print(st_)


Attributes
----------
Attributes are the variable that belongs to an object or the class

ex:
class how:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def nam(self):
        print(self.name)
        print(self.age)
s1 = how("lohi",23)
print(s1.nam())


class how:
    def details(self,name,age):
       self.name = name
       self.age = age
       
s1 = how()
s1.details("lohi",23)
print(s1.name)


Methods
-------
Methods are nothing but , function inside the class...

ex:
class calculator:
    def add(self,num,num_2):
        print(num + num_2)
    def sub(self,num,num_2):
        print(num - num_2)
cal = calculator()
cal.add(45,6)
cal.sub(8,6)



###########
self keyword
------------
self refers to current object...
ex:
class Test:
    def display(self):
        print(self)
te = Test()
print(te)
te.display()

consturctor or init
------------------- 
This constructor initializes the object automatically
when it is created ...

ex:
class batch:
    def __init__(self,name,branch):
        self.name = name
        self.branch = branch
    def display(self):
        print(self.name)
        print(self.branch)
B4 =batch('Lohi','ECE')
B4.display()        

Access sspecifiers
------------------
ex:
class batch:
    def __init__(self,name,branch):
        self._name = name
        self.branch = branch
    def display(self):
        print(self._name)
        print(self.branch)
B4 =batch('Lohi','ECE')
B4.display()        

ex:
class fam:
    def __init__ (self):
        self._name = 'Lohi'
        self._branch = 'CSE'
f = fam()
print(f._name)
print(f._branch)


#public Accessing:
class bank:
    def __init__(self):
        self.__pin = '6600'
AC = bank()
print(AC._bank__pin)


#private Accessing:
class Bank:
    def __init__(self):
        self.__pin = '6600'
    def display(self):
        print(self.__pin)
ac = Bank()
ac.display()


Encapsulation
-------------
Means wrapping the data and methods into single unit
(class while controlling access to the data)..

ex:
class atm:
    def __init__(self, balance):
        self._balance = balance
    def deposit(self,amount):
        self._balance += amount
        print(self._balance)
tran = atm(balance = int(input("enter amount: ")))
tran.deposit(amount = int(input("enter amount: ")))
        
'''





                 
