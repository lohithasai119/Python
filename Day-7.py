'''
Statements
----------
1.conditional statements
------------------------
i)if ---> used to check a condition is true or not
ex:
num = 10
if num % 2 == 0:
    print(f"{num} is a even number")
    

ii)if-else ---> else is the fall-back statement incase the if condition is false,
then this else will be executed... 
ex:
num = 9
if num % 2 == 0:
    print(f"{num} is even number")
else:
    print(f"{num} is odd number")

ex:
ICIC_details  = {"ATM PIN":'6600'}
pin = input("Enter your 4 digit ATM pin: ")
if pin in ICIC_details["ATM PIN"]:
    print("Welcome to ICIC ATM")
else:
    print("you have entered incorrect pin")


iii)nested if --->if inside the another if is called nested if.. 
ex:
ICIC_details  = {"ATM PIN":'6600'}
pin = input("Enter your 4 digit ATM pin: ")
if len(pin) == 4:
    if pin in ICIC_details["ATM PIN"]:
        print("Welcome to ICIC ATM")
    else:
        print("you have entered incorrect pin")
else:
    print("pls entered only 4 digit pin")


iv)elif ---> 
ex:
marks = int(input("enter your marks: "))
if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B+")
elif marks >= 60:
    print("B")    
elif marks >= 50:
    print("C")
else:
    print("Failed")


2.loop statements 
-----------------
i)for lopp --->a for loop used to itterate over a list, tuple, sequence...
***after for we can give any variable that is instance variable... 
ex:
any = (1,2,3,4,5)
for j in any:
    print(j)

any = [1,2,3,4,5]
for j in any:
    print(j)

any = "python is a language"
for j in any:
    print(j)

any = {"name":"lohi","role":"intern"}
for j in any.keys():
    print(j)

else in for loop
----------------
---> the else block will be executed after the loop, but incase the
loop is breaked then it will never entered in the else block..       
ex:
any = [1,2,3,4,5]
for j in any:
    print(j)
else:
    print("program ended")

ii)while loop ---> the while loop will execute untill the condition becomes true... 
ex:
i = 1
while i < 5:
    print(i)
    i += 1


3.control statements
--------------------
1.break ---> the break is used exit the loop ..
ex:
any = [1,2,3,4,5]
for j in any:
    print(j)
else:
    print("Entered")

    
any = [1,2,3,4,5]
for j in any:
    print(j)
    if j == 3:
        break
else:
    print("Entered")


2.continue --->The contiue will skip the current itteration..
ex:
any = [1,2,3,4,5]
for j in any:
    if j == 2:
        continue
    print(j)
else:
    print("Entered")


3.pass ---> space holder 
ex:
any = [1,2,3,4,5]
for j in any:
    if j == 3:
        continue
    print(j)
else:
    pass

any = [1,2,3,4,5]
for j in any:
    if j == 3:
        pass


range()
-------
---> range is built-in function that is used to generate a
sequence upto a limit.
syntax: range(start,end,step)
ex:
for j in range(1,20,2):
    print(j)


assert keyword
--------------
---> it will used to check the condition, but it will raise
an error incase it is false...
ex:
age = int(input("enter your age :"))
assert age >= 18,  "you must have 18 years"
'''













 
