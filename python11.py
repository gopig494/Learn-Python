# Types of def function Arguments
#formal and actual Arguments
def price(a,b):   #formal arguments
	return (a+b)
print(price(1000,200))   #actual arguments

#types of actual arguments
#Positional arguments
def price(a,b):
	return (a+b)
print(price(1000,200))

#Keyword arguments
#1.
def price(a,b):
	return (a-b)
print(price(b=1000,a=200))

#2.
def price(a,b,c):
	return (a+b+c)
print(price(1000,c=200,b=3000))

#3.
def price(a,b,c):
	return (a+b+c)
print(price(b=1000,a=200,3000))

#Default arguments
#1
def price(a=100,b=200,c=500):
	return (a+b+c)
print(price(1000,200))

#2
def price(a=100,b=200,c=500):
	print(a+b+c)
price(1000,c=200)

#3
def price(a=100,b=200,c=500):
	print(a+b+c)
price(b=1000,c=200)

#4
def price(a=100,b=200,c=500):
	print(a+b+c)
price(b=1000,2,c=200)

#5
def price(a=100,b=200,c=500):
	print(a+b+c)
price(1000,2,c=200)

#6
def price(a=100,b=200,c=500):
	print(a+b+c)
price()

#variable length argument
#1
def price(*a):
	print(a)
price(10,100,1)

#2
def price(*a):
	print(type(a))
price()

#3
def price(*a):
	for j in a:
		print(j)
price(10,20,30,40,50,60,70)

#4
def price(*a):
	i=0
	for j in a:
		i=i+j
	print(i)
price(10,20,30,40,50,60,70)

#5
def price(*a):
	for j in a:
		print(j)
price(10,[10,30],30,40,50,60,70)

#6
def price(b,*a):
	for j in a:
		print(j)
price(10,[10,30],30,40,50,60,70)

#7
def price(b,c,d=10,*a):
	print('b-',b)
	print('c-',c)
	print('d-',d)
	for j in a:
		print(j)
price(10,[10,30],30,40,50,60,70)

#8
def price(b,c,d=10,*a):
	print('b-',b)
	print('c-',c)
	print('d-',d)
	for j in a:
		print(j)
price(10,300)

#keyword variable length argument
#1
def price(**a):
	for a,b in a.items():
		print(a,b)	
price(a=10,b='gopi',c=300,d=1000)

#2
def price(**a):
	print(a)
price(a=10,b='gopi',c=300,d=1000)

#3
def price(**a):
	print(type(a))
price(a=10,b='gopi',c=300,d=1000)

#4
def price(g,**a):
	print(g)
	print(a)
price(100,a=10,b='gopi',c=300,d=1000)

#5
def price(g,t,f=0,**a):
	print(g)
	print(t)
	print(a)
price(100,t=2,a=10,b='gopi',c=300,d=1000)










