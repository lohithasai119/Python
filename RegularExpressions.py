'''
Regular Expressions(RegEx)
--------------------------
->RegEx is an sequence of char that can searching pattern..
->To use RegEx we have import re module..
syntax:-->import re

Functions
---------
1.findall() --> It will find all the char that are in the string...
ex:
import re
txt = 'python is a language and also called dynamically typed'
print(re.findall('[a]',txt))


2.search() --> This search() will find the char, but it will the first
               sequence that found in the string...
ex:
import re
txt = 'python is a language and also called dynamically typed'
print(re.search('[a]',txt))


3.split()
ex:
import re
txt = 'python is a language and also called dynamically typed'
print(re.split(' ',txt))


4.sub() --> like replace
ex:
import re
txt = 'python is a language and also called dynamically typed'
print(re.sub(' ','&',txt))


5.fullmatch() --> 
metachar
--------
[]
--
ex:
import re
txt = 'Python have 14 Versions'
print(re.findall('[a-z]',txt))
print(re.findall('[0-9]',txt))
print(re.findall('[A-Z]',txt))

print(re.search('[a-z]',txt))
print(re.search('[0-9]',txt))
print(re.search('[A-Z]',txt))


^
--
ex:
import re
txt = 'Python have 14 Versions'
print(re.findall('^Python have',txt))
print(re.search('^have',txt))
print(re.search('^Python have',txt))


$
--
ex:
import re
some = 'I am going to school'
print(re.findall('I$',some))
print(re.findall('school$',some))
print(re.search('school$',some))


.
--
ex:
import re
any_ = 'Hello! This is lohi'
print(re.findall('l..i',any_))
print(re.findall('l...',any_))
print(re.findall('...s',any_))
print(re.search('T...',any_))


*
--
ex:
import re
how = 'python module will going to complete this week'
print(re.findall('p.*',how))
print(re.findall('p.*n',how))
print(re.findall('p.*ython.',how))
print(re.search('p.*n',how))


+
--
ex:
import re
how = 'python is a language'
print(re.findall('p.+',how))
print(re.findall('p.+thon',how))
print(re.search('p.+n',how))
print(re.search('p.+a',how))


{} 
--
import re
now = 'python is a language'
print(re.findall('p.{6}',now))
print(re.findall('p.{100}',now))
print(re.search('p.{2}',now))
print(re.search('p.{5}',now))


'''








