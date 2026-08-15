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



'''



















                 
