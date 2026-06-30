'''
Type conversions
----------------
---> This process of converting one data type to another..
i)Int-->string;float
ex:
num =89
num_2 = float(num)
print(num_2)
print(type(num))
so = str(num)
print(type(so))


ii)float-->string;integer
ex:
num =8.9
how = str(num)
print(how)
print(type(how))
num_2 = int(num)
print(num_2)


iii)string-->integer;float;list;tuple
ex:
hai ='78'
num = int(hai)
print(num + 10)
print(type(num))

hello = '67.89'
num_2 = float(hello)
print(num_2)

any_ = "2596"
con_ = list(any_)
print(con_)

any_ = "2596"
con_ = tuple(any_)
print(con_)


iv)list-->string;tuple;dictionary
ex:
var_ = ['p','y','t','h','o','n']
text_="".join(var_)
print(text_)

var_ = ['p','y','t','h','o','n']
some = tuple(var_)
print(some)

pyth = [('a',1),('b',8)]
conver = dict(pyth)
print(conver)

v)tuple-->string;list
ex:
fam = (1,2,3,4)
num = list(fam)
print(num)

fam = ('h','e','l','l','o')
num = "".join(fam)
print(num)



built-in-functions
------------------
str()
float()
int()
list()
tuple()


'''



















