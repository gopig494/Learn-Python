#Addtion of numbers in given range
def add(a,b):
	b=b+a
	if a==1:
		print(b)
	elif a>1:
		add(a-1,b)
add(range,0)

#Factories
#1
def add(a,b):
	b=b*a
	if a==1:
		print("The Factoriel of Given Range  :",b)
	elif a>1:
		add(a-1,b)
r=int(input("Enter the range :"))
add(r,1)

#2
def add(a):
	if a==1:
		return 1
	else:
		return a*add(a-1)
r=int(input("Enter the range :"))
print("The Factoriel of Given number  :",add(r))

#Diff b/w print() and return function while function calling
#print
#1
a=10
def b(a):
	print("Any 1")
b(a)

#2
a=10
def b(a):
	print(a+10)
b(a)

#return
#1
a=10
def b(a):
	return 20
c=b(a)
print(c)
#2
a=10
def b(a):
	return a*20
c=b(a)
print(c)

#fibonacci series
def fbb(a,b,c):
	m=a+b
	print(m)
	a=b
	if c>1:
		b=m
		fbb(a,b,c-1)
p=int(input("Enter the 1st value :"))
q=int(input("Enter the 2nd value :"))
r=int(input("Enter the fibonacci Range :"))
fbb(p,q,r)

#Perfect Number
def per(a,i,tot):
	if i<a:
		if a%i==0:
			tot=tot+i
		i+=1
		per(a,i,tot)
	else:
		if tot==a and a!=0:
			print("THe given number is Perfect number  :",a)
		else:
			print("The given number is not perfect")
p=int(input("Enter the number :"))
per(p,1,0)

