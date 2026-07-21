'''
Error Handling
--------------
1.Syntax error
--------------
ex:
for j in range(1,10:
    print(j)

output--->SyntaxError

2.Identation error
------------------
ex:
for j in range(a):
    print(j)
else:
print()

output-->IndentationError

3.Valu error
------------
ex:
num = int(input('Enter a num: "))

output--->ValueError


Exception Handling
------------------
try
---
The try block will test the code error
syntax-- try:

except
------
This except let us handle the errors in the code
syntax-- except:

ex:
try:
    print(num)
except:
    print('will get name error')


ex:
try:
    num = int(input("Enter a num: "))
except NameError:
    print('will get name error')


ex:
try:
    num = int(input("Enter a num: "))
except ValueError:
    print('will get name error')


ex:
try:
    num = int(input("Enter a num: "))
    num_2 = int(input("Enter a num: "))
    print(num/num_2)
except:
    print('will get zerodivision error')



ex:
try:
    num = int(input("Enter a num: "))
    num_2 = int(input("Enter a num: "))
    print(num/num_2)
except:
    print('will get zerodivision error')
except ValueError:
    print('will get value error')




else
----
If the try block does not have any error than the else block will execute

ex:
try:
    num = int(input("Enter a num: "))
    num_2 = int(input("Enter a num: "))
    print(num/num_2)
except ZeroDivisionError:
    print('will get zerodivision error')
except ValueError:
    print('will get value error')
else:
    print('no error')




finally
-------
The finally block either code contain errors or not

ex:
try:
    num = int(input("Enter a num: "))
    num_2 = int(input("Enter a num: "))
    print(num/num_2)
except ZeroDivisionError:
    print('will get zerodivision error')
except ValueError:
    print('will get value error')
else:
    print('no error')
finally:
    print('end')


'''
try:
    num = int(input("Enter a num: "))
    num_2 = int(input("Enter a num: "))
    print(num/num_2)
except ZeroDivisionError:
    print('will get zerodivision error')
except ValueError:
    print('will get value error')
else:
    print('no error')
finally:
    print('end')




















