''' 
Inheritance
-----------
Inheritance is an oop concept where one class (child/derived)
acquired the properities and methods of another class(parent/base)


class parenr:
    pass
class child(parent):
    pass

Types of Inheritance
--------------------
1.single inheritance
--------------------
A child class inherits from one parent is single inheritance
ex:
class animal:
    def sound(self):
        print('Animals make sounds')
class dog(animal):
    def barks(self):
        print("Dog barks")

d = dog()
d.sound()
d.barks()

ex:
class father:
    def land(self):
        print('5 ar of land')
class son(father):
    def flat(self):
        print('3BHK flat')
s = son()
s.land()
s.flat()

2.Multiple inheritance
----------------------
A child inherits more than one parent iscalled multiple inheritance.

ex:    
class father:
    def skills(self):
        print('Driving')
class mother:
    def talent(self):
        print('cooking')
class brother:
    def learn(self):
        print('fighting')
class son(father,mother,brother):
    def mine(self):
        print('web development')

all_ = son()
all_.skills()
all_.learn()
all_.talent()
all_.mine()


3.Multi-level Inheritance
-------------------------
One child class becomes the parent for another class

ex:
class grandfather:
    def house(self):
        print('Own house')
class father(grandfather):
    def flat(self):
        print('New 3BHK flat')
class son(father):
    def car(self):
        print('Have a car')
fam = son()
fam.house()
fam.flat()


4.Hierarchical
--------------
Multiple childs inherits from the same parent

ex:
class mother:
    def gold(self):
        print('10 KG gold')
class pinky(mother):
    def show(self):
        print('will get 5kg gold')
class chutky(mother):
    def show_2(self):
        print('will get remaining 5kg gold')

child_1 = pinky()
child_2 = chutky()

child_1.gold()
child_1.show()

child_2.gold()
child_2.show_2()


ex:
class father:
    def land(self):
        print('60 arc land')
class suresh(father):
    def arc(self):
        print('20 arc land')
class ramesh(father):
    def arc_2(self):
        print('20 arc land')
class somesh(father):
    def arc_3(self):
        print('will get remianing arc')

child_1 = suresh()
child_2 = ramesh()
child_3 = somesh()

child_1.land()
child_1.arc()
        
child_2.land()
child_2.arc_2()
        
child_3.land()
child_3.arc_3()

        
        
5.Hybrid inheritance
--------------------
This is the combination of two or more types of inheritance example of
multiple + multi-level

ex:
class A:
    def methodA(self):
        print('class A')
class B(A):
    def methodB(self):
        print('Class B')
class C(A):
    def methodC(self):
        print('Class C')        
class D(B,C):
    def methodD(self):
        print('Class D')

so = D()
so.methodA()
so.methodB()
so.methodC()


6.Super()
---------
This super() function is used to access the parent class
methods or constructor in the child class...

ex:
class parent:
    def show(self):
        print('parent')
class child(parent):
    def show(self):
        super().show()
        print('child class')

chi_ = child()
chi_.show()


ex:
class person:
    def __init__(self,name):
        self.name = name
class student(person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll = roll
    def display(self):
        print(self.name)
        print(self.roll)
an = student('Lohi',101)
an.display()

'''





