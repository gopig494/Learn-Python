#Define a Function
def call(a):
    print(a)
  
#Function call
def call(a):
    print(a)
call(2)

#return and print
def call(a):
	print(a)
call(2)

def call(a):
	return 2000
print(call(2))

#Docstring
def call(a):
	'''The function call is used to return a valuef 2000'''
	return 2000
print(call(2))

#Pass
def call(a):
	pass
print(call(2))

#Recursive Function call()
def call(a,b):
	print(a+b)
	a+=1
	if a<=10:
	call(a,b)
call(1,2)

#factorial program
def call(a):
	if a==1:
		return 1
	else:
		return a * call(a-1)
print(call(3))

#Factorial Program Using user define function and loops:
inp=int(input("Enter the Range  :"))
def fact(inp):
    a=inp
    fact=1
    while inp>0:
        fact=fact*inp
        inp-=1
    else:
        print('Factorial of ', a ,'is', fact)
for i in range(1,inp+1):
    fact(i)
    
#reverse order factorial
inp=int(input("Enter the Range  :"))
def fact(inp):
    a=inp
    fact=1
    while inp>0:
        fact=fact*inp
        inp-=1
    else:
        print('Factorial of ', a ,'is', fact)
for i in range(inp,0,-1):
    fact(i)
    
#Addition of factorials of given range
inp=int(input("Enter the Range  :"))
def fact(inp):
    a=inp
    fact=1
    while inp>0:
        fact=fact*inp
        inp-=1
    else:
        #print('Factorial of ', a ,'is', fact)
        return fact
t=0
for i in range(1,inp+1):
   	fact(i)
	t=t+fact(i)
else:
    print(t)
	
#print the additon of factorial reverse order
inp=int(input("Enter the Range  :"))
def fact(inp):
    a=inp
    fact=1
    while inp>0:
        fact=fact*inp
        inp-=1
    else:
        #print('Factorial of ', a ,'is', fact)
        return fact
def rev(a):
    while a>0:
        b=a%10
        if a>9:
            print(b,end="")
            a=a//10
        else:
            print(b)
            a=a//10       
t=0
for i in range(1,inp+1):
    fact(i)
    t=t+fact(i)
else:
    rev(t)
	
#Add the additon of factorial of  reverse order digits
inp=int(input("Enter the Range  :"))
def fact(inp):
    a=inp
    fact=1
    while inp>0:
        fact=fact*inp
        inp-=1
    else:
        #print('Factorial of ', a ,'is', fact)
        return fact
def rev(a):
    to=0
    while a>0:
        b=a%10
        to=to+b
        a=a//10
    else:
        print(to)
             
t=0
for i in range(1,inp+1):
    fact(i)
    t=t+fact(i)
else:
    rev(t)

#Add the additon of factorial of  reverse order digits
#and again add the result of addition when it exceed above one digit
inp=int(input("Enter the Range  :"))
def fact(inp):
    a=inp
    fact=1
    while inp>0:
        fact=fact*inp
        inp-=1
    else:
        #print('Factorial of ', a ,'is', fact)
        return fact
def rev(a):
    to=0
    while a>0:
        b=a%10
        to=to+b
        a=a//10
    else:
        if to>9:
            rev(to)
        else:
            print(to)
             
t=0
for i in range(1,inp+1):
    fact(i)
    t=t+fact(i)
else:
    rev(t)