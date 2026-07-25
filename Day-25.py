'''
matplotlib
-----------
matplotlib library is an python library that provides
functionality to charts, grphs, bar and data visualization.

ex:
import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [10,20,15,30,5]

plt.plot(x,y)
plt.title('simple plot')
plt.show()


ex:
import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [10,20,15,30,5]

plt.plot(x,y)
plt.title('simple plot')
plt.xlabel('Xaxis')
plt.ylabel('Ylabel')
plt.show()


#sales of cars
ex:
import matplotlib.pyplot as plt
x = [2026,2024,2025,2023,2021]
y = [10,20,15,30,5]

plt.plot(x,y)
plt.title('car sales')
plt.xlabel('years')
plt.ylabel('number of cars')
plt.show()


Bar plot
--------
ex:
import matplotlib.pyplot as plt
x = [2026,2024,2025,2023,2021]
y = [10,20,15,30,5]

plt.bar(x,y)
plt.title('car sales')
plt.xlabel('years')
plt.ylabel('number of cars')
plt.show()

ex:
import matplotlib.pyplot as plt
x = [2026,2024,2025,2023,2021]
y = [10,20,15,30,5]

plt.bar(x,y,colors='red',edgecolor='black')
plt.title('car sales')
plt.xlabel('years')
plt.ylabel('number of cars')
plt.show()


pie plot
--------
import matplotlib.pyplot as plt
subjects_ = ['python','java','c']
stu_ = [20,50,30]

plt.pie(stu_,labels=subjects_,colors=['red','yellow','green'],autopct='1%.1f%%')
plt.legend(subjects_)
plt.title('courses')
plt.show()



scatter plot
------------
ex:
import matplotlib.pyplot as plt
x = ['BMW','swift','Toyoto']
y = [120,150,135]

plt.scatter(x,y,color='red')
plt.title('car sales')
plt.xlabel('years')
plt.ylabel('number of cars')
plt.show()



Histogram plot
--------------
import matplotlib.pyplot as plt
y = [10,40,20,50]

plt.hist(y,bins=20)
plt.title('car sales')
plt.xlabel('years')
plt.ylabel('number of cars')
plt.show()

'''


import matplotlib.pyplot as plt
x = [2026,2024,2025,2023,2021]
y = [10,20,15,30,5]

plt.plot(x,y)
plt.title('car sales')
plt.xlabel('years')
plt.ylabel('number of cars')
plt.show()

# bar
x = [2026,2024,2025,2023,2021]
y = [10,20,15,30,5]

plt.bar(x,y,colors='red',edgecolor='black')
plt.title('car sales')
plt.xlabel('years')
plt.ylabel('number of cars')
plt.show()


#pie
import matplotlib.pyplot as plt
x = [2026,2024,2025,2023,2021]
y = [10,20,15,30,5]

plt.bar(x,y,colors=['red','yellow','green'],autopct='1%.1f%%')
plt.title('car sales')
plt.xlabel('years')
plt.ylabel('number of cars')
plt.show()


#Histogram
y = [10,20,15,30,5]

plt.hist(y,bins=20)
plt.title('car sales')
plt.xlabel('years')
plt.ylabel('number of cars')
plt.show()


#scatter
x = [2026,2024,2025,2023,2021]
y = [10,20,15,30,5]

plt.scatter(x,y,color='red')
plt.title('car sales')
plt.xlabel('years')
plt.ylabel('number of cars')
plt.show()
