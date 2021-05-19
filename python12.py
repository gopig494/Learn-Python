#function
#Variables
#1
phone='iphone,xiomi'  #phone_variable
print(phone)

#types of variables
#Global variables
#1
phone='iphone,xiomi'
def ph():
    print(phone)

def sm():
    print(phone)
	
def call():
    sub_variable=phone
    print(sub_variable)
ph()
sm()
call()

#2
phone='iphone,xiomi',100,[10,20,30,40]
def ph():
    print(phone)

def sm():
    print(phone)
	
def call():
    sub_variable=phone
    print(sub_variable)
ph()
sm()
call()

#3
phone='iphone,xiomi',100,[10,20,30,40]
def ph():
    print(phone)

def sm():
    print(phone)
	
def call():
    sub_variable=phone
    print(sub_variable)

def con():
    sub_variable=phone
    a=sub_variable[0]+str(sub_variable[1])
    print(a)

ph()
sm()
call()
con()

#Local Variable

def ph():
	phone='iphone,xiomi'
	print(phone)
def sm():
	phone=2000,10000
	print(phone)
	
def call():
	phone='iphone',100,'moto'
	sub_variable=phone
	print(sub_variable)

def con():
	phone='redmi'
	sub_variable=phone
	a=sub_variable[0]+str(sub_variable[1])
	print(a)

ph()
sm()
call()
con()

#using local and global variables 
#1
phone=1,2,3,4,5,6,7,8,9,10
def ph():
	global phone 
	phone='iphone,xiomi'
	print(phone)
def sm():
	print(phone)
def call():
	sub_variable=phone
	print(sub_variable)
ph()
sm()
call()

#2
phone=1,2,3,4,5,6,7,8,9,10
def ph():
	global phone 
	phone='iphone,xiomi'
	phone=1,2,3,4,5,6,7,8,9,10
	print(phone)
def sm():
	print(phone)
def call():
	sub_variable=phone
	print(sub_variable)
ph()
sm()
call()

#3
#use global variable inside the function 
#while the local variable already in the same function
phone=1,2,3,4,5,6,7,8,9,10
def ph():
	phone='iphone,xiomi'
	phone=globals()['phone']
	print(phone)
def sm():
	print(phone)
def call():
	sub_variable=phone
	print(sub_variable)
ph()
sm()
call()

#Lambda or Anonymous function
#1
phone=lambda a,b:print(a+b)
phone(10,10)
phone(1,1)

#2
def myfunc(n):
	c=lambda a : a * n
	return c(5)
print(myfunc(5))

#3
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

#4
def ma(n):
  return lambda a : a * n if a>n else a-n

m = ma(2)

print(m(11))

#5
def ma(n):
  return lambda a : a * n if a>n else a-n

m = ma(200)

print(m(11))

#6
def ma(n):
  return lambda a :print( a * n if a>n else a-n)

m = ma(200)

m(11)