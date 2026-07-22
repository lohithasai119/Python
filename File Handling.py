'''
File Handling
-------------
File handler is an object that gives more options like
creating,updating...

Two ways to open the file:-

1.Open()
--------
sytax:
do = open('file_name','mode')
close()

ex:
do = open('F:/python/coding/doubts.py','r'):
print(do.read())


2.with(keyword)
---------------
syntax:
withopen('file_name','mode')as do:

ex:
with open('F:/python/coding/doubts.py','r')as do:
    print(do.read())



Modes
-----
r --> used to read the file,incase if the is not present it will
     raise error...
ex:
with open('F:/mysql/MySQL-cls notes/Day-9.txt','r')as do:
    print(do.read())
     
w --> used to write the text inside the file...
ex:
with open('F:/mysql/MySQL-cls notes/Day-9.txt','w')as do:
    print(do.write('you look so beautiful today'))

a --> Append is used to add the text at last position
     inside the file..     
ex:
with open('F:/mysql/MySQL-cls notes/Day-9.txt','a')as do:
    print(do.write('we are use file handling'))

x --> used to create a new by adding the inside the file,
      incase if the file is present it will raise an error..
ex:
with open('F:/mysql/MySQL-cls notes/Day-9.txt','x')as do:
    print(do.write('we are use file handling'))


functinalities:-
--------------
write()
-------
This function is used to add the text inside a file or update
a file with new text...

ex:
with open('F:/mysql/MySQL-cls notes/Day-9.txt','w')as do:
    print(do.write('you look so beautiful today'))

ex:
with open('F:/mysql/MySQL-cls notes/Day-9.txt','a')as do:
    print(do.write('you look so beautiful today'))


read()
-----
This is used to read a file and this read() will read file chunk
by chunk and we can also specify the size...

ex:
with open('F:/mysql/MySQL-cls notes/Day-9.txt','r')as do:
    print(do.read(5))


readline()
---------
This readline() will read only one line at a time...

ex:
with open('F:/mysql/MySQL-cls notes/Day-9.txt','r')as do:
    print(do.readline())


readlines()
-----------
This readlines() will read whole file and give it in a list
each line is one index in the list....

ex:
with open('F:/mysql/MySQL-cls notes/Day-9.txt','r')as do:
    print(do.readlines())


'''







