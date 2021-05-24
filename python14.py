#modules and Packages 
#modules and packages are in same location 
#module
#1
from math import factorial
print(factorial(5))

#2
import math
print(math.factorial(5))

#3
from math import *
print(factorial(5))

#4
from math import factorial as a
print(a(5))

#5
import math as a 
print(a.factorial(5))

#6
from math import factorial,floor 
print(factorial(5))
print(floor(5.55))

#7
from math import factorial as a,floor as b
print(a(5))
print(b(5.55))

#Access User Created Modules and variables in Same Locations
#modules
#1
import fun
print(fun.variable)

#2
import fun
print(fun.d())

#3
import fun
fun.e()

#Packages 
#1
from packages import fun
print(fun.d())

#2
from packages import fun,fun2
fun2.sample()

#Modules and Packages are in different location
#1
import sys
sys.path.insert(0,'/home/gopi/Music')
from packages import fun
print(fun.d())

#Module Functions
#find what are the functions and variables are in the same module
#1
print(dir())

#2
import math 
print(dir(math))

#3
import os
print(dir(os))

#4
import sys
print(dir(sys))

#Important Modules

#1
import os

print(os.getcwd())
a=os.path.abspath(__file__)
print(a)
print(os.path.dirname(a))

#2
import os
os.mkdir('/home/gopi/Documents/test')

#3
import os
os.rmdir('/home/gopi/Documents/test')
