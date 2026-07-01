'''
Input formatting from user
--------------------------
1.input()
--------
--> the input() function is used to take input from the user...

i)int
-----
ex:
num = int(input("Enter a number: "))
num_2 = int(input("Enter a number: "))
print(num + num_2)

ii)string
---------
ex:
how = input("Enter a char: ")
print(how + "lohi")

iii)float
---------
ex:
num = float(input("Enter your salary: "))
print(num, "is the monthly salary")

iv)list
-------
ex:
group = list(map(int,input().split()))
print(group)

group = list(map(input().split()))
print(group)

v)Tuple
-------
ex:
group = tuple(map(int,input().split()))
print(group)

group = tuple(map(input().split()))
print(group)


**eval method
-------------
num = eval(input("Enter: "))
print(type(num))


**f method
----------
num = input("Enter your name: ")
age = int(input("Enter your age: "))
print(num,"your age is ",age)
print(f"{num} your age is {age + 3}")


**modulus format
----------------
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("my name is  %s and i'm %d years old" % (name,age))


'''


name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("my name is  %s and i'm %d years old" % (name,age))

