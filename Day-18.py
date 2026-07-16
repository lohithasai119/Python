'''
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





                 
