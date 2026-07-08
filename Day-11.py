'''
Lambda function
---------------
---> This is also called as annonymous function...
---> A lamda function can take n number of arguments but
having only one expression...

Syntax:
lambda arguments: expression

ex:
some = lambda an,so,why : an + so + why
print(some(10,8,3))


filter()
-------
---> The filter() function is a built-in function used to filter
elements from an itterables such as list, tuple and set based on condition...
--->This filter() function returns filter object so we can convert that into
list, set and tupe..

syntax:
filter(function, itterable)

ex:
nums = [1,2,3,4,5]
rev = filter(lambda a : a % 2 == 0, nums)
print(list(rev))

nums = [1,2,3,4,5]
rev = filter(lambda a : a % 2 != 0, nums)
print(list(rev))


List Comprehension
------------------
---> This offers a shorter syntax when we want to create a new list from
the old list...

syntax:
variable_name = [expression loop condition]

ex:
old_ = [1,2,3,4,5,6]
new_ = [j for j in old_] 
print(new_)

old_ = [1,2,3,4,5,6]
new_ = [j for j in old_ if j % 2 == 0]
print(new_)


Dictionary Comprehension
------------------------
--->This offers a shorter syntax when we want to create a new dict from
the old dict...

syntax:
variable_name = [expression loop]

ex:
old_dict = {1:2, 3:7, 5:6}
new_dict = {i:j for (i,j) in old_dict.items() if j % 2 == 0}
print(new_dict)


'''
old_dict = {1:2, 3:7, 5:6}
new_dict = {i:j for (i,j) in old_dict.items() if j % 2 == 0}
print(new_dict)





























