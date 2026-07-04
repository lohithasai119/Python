'''
#palindrom
so = input("Enter your word :")
empty = ""
for j in so:
    empty = j + empty
if empty == so:
    print(f"{so} is a palindrom")
else:
    print(f"{so} is not a palindrom")


#fibonacci series
num = 0
num2 = 1
limit = int(input("enter your number: "))
print(num,num2,end = " ")
for i in range(1,limit+1):
    all = num + num2
    num = num2
    num2 = all
    print(all,end = " ")


#calculator
val = int(input("enter number: "))
val2 = int(input("enter number: "))
user_in = int(input("enter \n1.add \n2.sub \n3.mul \n4.pow "))
if user_in == 1:
    print(val + val2)
elif user_in == 2:
    print(val - val2)
elif user_in == 2:
    print(val - val2)    
elif user_in == 3:
    print(val * val2)
else:
    print(val ** val2)
    
# tables
table = int(input("enter a number: "))
for val in range(1,11):
    print(f"{table} x {val} = {table * val}")


#perfect number
num =  int(input("enter a number: "))
sum = 0
for j in range(1,num):
    if num % j == 0:
        sum += j
if sum == num:
    print(f"{num} is a perfect number")
else:
    printt(f"{num} not a perfect number")
    
'''














