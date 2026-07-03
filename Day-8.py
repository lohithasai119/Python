'''
# prime number
num = int(input("enter a number :"))
count = 0
for j in range(1,num+1):
    if num % j == 0:
        count += 1
if count == 2:
    print(f"{num} is a prime")
else:
    print(f"{num} is not a primt")



# upto --- prime numbers
limit = 20 
for j in range(1,limit+1):
    count = 0
    for i in range(1,j+1):
        if j % i == 0:
            count += 1
    if count == 2:
        print(f"{j} is a prime")



#right angle triangle
num = 5
for j in range(1,num+1):
    for i in range(1,j+1):
        print("*", end = " ")
    print()


num = 5
for j in range(1,num+1):
    for i in range(1,j+1):
        print(j, end = " ")
    print()

num = 5
for j in range(1,num+1):
    for i in range(1,j+1):
        print(i, end = " ")
    print()


num = 4
count = 0
for j in range(1,num+1):
    for i in range(1,j+1):
        count += 1
        print(count, end = " ")
    print()


num = 4
count = 0
for j in range(num,0,-1):
    for i in range(1,j+1):
        print(i, end = " ")
    print()


num = 4
count = 0
for j in range(num,0,-1):
    for i in range(1,j+1):
        print(" ",i, end = " ")
    print()
    

# Amstrong number
am_str = 153
length = len(str(am_str))
all_sum = 0
for j in str(am_str):
    all_sum += int(j) ** length
if all_sum == am_str:
    print(f"{am_str} is amstrong number")
else:
    print(f"{am_str} is not amstrong number")


# pyramid
num = 6
for j in range(num):
    print(" " * (num - j - 1),end = " ")
    print("* " * (2 * j + 1))



num = 5

for j in range(num, 0, -1):
    for space in range(num-1-j):
        print(" ", end=" ")
    for star in range(j):
        print("*", end=" ")
    print()


num = 5
count = 1
for j in range(1, num + 1):
    print("  " * (num - j), end="")
    for i in range(2 * j - 1):
        print(f"{count:2}", end=" ")
        count += 1
    print()

'''

num = 5
count = 1
for j in range(1,num+1):
    print("  " * (num-j),end="")
    for i in range(2*j-1):
        print(count,end = " ")
        count += 1
    print()
    




