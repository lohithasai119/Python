'''
Generators
----------
--->This generator is special function that returns the itertor.
instead of returning all the values at once...
---> here we are going to use yield keyword
ex:
def some():
    yield 1
    yield 2
    yield 3
    
So = some()
print(next(So))
print(next(So))
print(next(So))


working of generator
--------------------
---> when a function called...
---> It doesn't execute the funtion immediately...
---> It will returns the generator the object...
---> Then the funtion will pauses at each yield...
---> When the next() is called again, execution resumes from
where it stopped..
ex:
def demo():
    print("start")
    yield 1

    print("middle")
    yield 2

    print("end")
    yield 3

how = demo()
print(next(how))
print(next(how))


with generators
---------------
def how(so):
    for i in range(so):
        yield i * i
any_ = how(5)        
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))    


without generator
-----------------
def sqt(n):
    for j in range(n):
        print(j * j)
sqt(5)

#difference btw function and generator
function
--------
->return
->return complete result
->function will end after the return the values 
->more memory usage
->This function never resume 

generator
---------
->yield
->return one value at once
->pauses after every yield
->Less memory usage
->Resume after next()

yield keyword
-------------
---> This will produces the value
---> but the yield pauses the function
---> And yield will save the functions current state 
---> yield will continue were it stopped...
ex:
def how(so):
    for i in range(so):
        yield i * i
any_ = how(5)        
print(next(any_))
print(next(any_))


next() keyword
--------------
---> The next() function is used to retrieve the next value
from a generator...
ex:
def how(so):
    for i in range(so):
        yield i * i
any_ = how(5)        
print(next(any_))
print(next(any_))

StopIteration 
--------------
--->calling next function after all values retrieve
than it will raise StopIteration exception...
ex:
def how(so):
    for i in range(so):
        yield i * i
any_ = how(5)        
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))

Generator Expression
--------------------
--->The generator expression is similar to a list comprehension
parenthesi () insted of []
ex:
gen = (x*x for x in range(4))
print(next(gen))
print(next(gen))

'''





