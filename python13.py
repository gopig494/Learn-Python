#lambda.....Filter(),map(),reduce()- functions
#Filter()

#lambda
#1
l=('a','aa','1','1010','2000')
print(tuple(filter(lambda m:True if m>='a' and m<='z' else False,l)))

#2
l=[10,20,30,40,50,60,70]
print(tuple(filter(lambda m:True if m%7==0 else False,l)))

#user define function
#1

l=[10,20,30,40,50,60,70]
def divide(b):
	if b%7==0:
		return True
	else:
		return False
print(list(filter(divide,l)))

#2
l=[10,20,30,40,50,60,70]
def divide(b):
	if b%7==0:
		return b
	else:
		return False
print(list(filter(divide,l)))

#3
l=[10,20,30,40,50,60,70]
def divide(b):
	if b%7==0:
		return False
	else:
		return b
print(list(filter(divide,l)))

#4
l=[10,20,30,40,50,60,70]
def divide(b):
	if b%7==0:
		return 25423453453453
	else:
		return False
print(list(filter(divide,l)))

#5

l=[10,20,30,40,50,60,70]
def divide(b):
	if b%7==0:
		return 'v'
	else:
		return False
print(list(filter(divide,l)))

#6
l=[10,20,30,40,50,60,70]
m=[10,20,30,40,50,60,70]
def divide(b,m):
	if b%7==0:
		return 'v'
	else:
		return False
print(list(filter(divide,l,m)))

#7
l=(10,20,200,1400,10000,60,70)

def divide(b):
	if b%7==0:
		return True
	else:
		return False
print(list(filter(divide,l)))

#8
l=('raja',10,1.2)

def divide(b):
	if type(b)==str:
		return False
	else:
		return True
print(tuple(filter(divide,l)))

#9
l=('a','aa','1','1010','2000')

def divide(b):
	if b >='a' and b <='z':
		return False
	else:
		return True
    
#10
l=('a','aa','1','1010','2000')

def divide(b):
	if b >='a' and b <='z':
		return True
	else:
		return False
print(tuple(filter(divide,l)))

#map
#1
l=[1,2,3,4,5]
m=[6,7,8,9,10]
s=list(map(lambda a:a*a ,l)
print(s)
       
#2
l=[1,2,3,4,5]
m=[6,7,8,9,10]
s=list(map(lambda a:'k',l))
print(s)
       
#3
l=[1,2,3,4,5]
m=[6,7,8,9,10]
s=list(map(lambda a,b:'k',l,m))
print(s)
   
#4
 l=[1,2,3,4,5]
m=[6,7,8,9,10]
n=[6,7,8,9,10]
s=list(map(lambda a,b,c:a+b+c,l,m,n))
print(s)
	   
#5
l=[1,2,3,4,5]
m=(6,7,8,9,10)
n={6,7,8,9,10}
s=list(map(lambda a,b,c:a+b+c,l,m,n))
print(s)
	   
#6
l=[1,2,3,4,5]
m=(6,7,8,9,10)
n={6,7,8,9,10}
s=list(map(lambda a,b,c:a/2,l,m,n))
print(s)
	
#reduce()
#1
from functools import reduce
l=[1,2,3,4,5]
m=(6,7,8,9,10)
n={6,7,8,9,10}
s=reduce(lambda a,b:a+1,l)
print(s)
	   
#2
from functools import reduce
l=[1,2,3,4,5]
s=reduce(lambda a,b:a+1,l,5)
print(s)
	   
#3
from functools import reduce
l=[1,2,3,4,5]
s=reduce(lambda a,b:a+b,l)
print(s)
	
#Aliasing name of a function
#1
def gopi():
	print("developer")
mani=gopi


mani()
gopi()
	   
#2
def gopi():
	print("developer")
	
mani=gopi()


mani
gopi()
	   
#3
def gopi(a):
	print("developer",a)
kavin=gopi
kavin('good')
	
#4
a=print
a(1)
	   
#nested function
#1
def fun():
	print("out")
	def fun():
		print("in")
	fun()
fun()

#2
def fun():
	print("out")
	def fun():
		return 'in'
	print(fun())
fun()

#3
def fun():
	def fun():
		return 'in'
	return fun()
print(fun())

	
	


       