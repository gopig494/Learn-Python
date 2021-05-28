#Types of methods in oops 
#instance method 
#1
class method:
	def fun(self):
		print('hi i am instance method')
a=method()
a.fun()

#2
class method:
	def fun(self,a,b):
		self.no1=a
		self.no2=b
		
a=method()
a.fun(1,2)
print(a.no1)
print(a.no2)

#3
class method:
	def fun(self,a,b):
		self.no1=a
		self.no2=b
		
a=method()
a.fun(1,2)
print(a.no1)
a.no1=1000
print(a.no1)

#4
class method:
	def fun(self,a,b):
		self.no1=a
		self.no2=b
		value=5000
		print(value)
		
a=method()
a.fun(1,2)
print(a.no1)
a.no1=1000
print(a.no1)

#5
class method:
	def fun(instance,a,b):
		instance.no1=a
		instance.no2=b
		
a=method()
a.fun(1,2)
print(a.no1)

#class variables
#Before creating constructor
#1
class method:
	name='gopi'
	no=494
	def fun(self):  #self instance
		print('hi i am method')
gopal=method()
print(method.name)
method().fun()

#after creating constructor
#we can't access the instance method after creating 
#the constructor
#1
class method:
	name='gopi'
	no=494
	def __init__(self,a,b):
		self.a=a
		self.b=b
	def fun(self):
		print('hi i am method')
gopal=method(10,20)
print(method.name)
#method().fun()
gopal.fun()

#class method
#after creating class method 
#access by class
#1
class method:
	name='gopi'
	no=494
	def __init__(self,a,b):
		self.a=a
		self.b=b
	@classmethod	
	def fun(cls):
		print('hi i am method')
gopal=method(10,20)
method.fun()
#access by instance
#1
class method:
	name='gopi'
	no=494
	def __init__(self,a,b):
		self.a=a
		self.b=b
	@classmethod	
	def fun(cls):
		print('hi i am method')
gopal=method(10,20)
gopal.fun()

#static method 
#1
class method:
	name='gopi'
	no=494
	#def __init__(self,a,b):
	#	self.a=a
	#	self.b=b
	@staticmethod	
	def fun():
		print('hi i am method')
	#fun()
		
#gopal=method(10,20)
fun()

#2
class method:
	name='gopi'
	no=494
	#def __init__(self,a,b):
	#	self.a=a
	#	self.b=b
	@staticmethod	
	def fun():
		print('hi i am method')
		method.fun()
		
#gopal=method(10,20)
method.fun()

#3
class method:
	name='gopi'
	no=494
	def __init__(self,a,b):
		self.a=a
		self.b=b
	@staticmethod	
	def fun():
		print('hi i am method')
		gopal.obj()  #instance method call
		method.clss() #class method call
	def obj(self):
		print("i am object ")
	@classmethod
	def clss(cls):
		print("i am class")

gopal=method(10,20)
method.fun()

#4
class method:
	name='gopi'
	no=494
	def __init__(self,a,b):
		self.a=a
		self.b=b
	@staticmethod	
	def fun():
		method.name='indian'
		gopal.a=5000
	def obj(self):
		print("i am object ")
	@classmethod
	def clss(cls):
		print("i am class")
	
		
gopal=method(10,20)
print(method.name)
print(gopal.a)
method.fun()
print(method.name)
print(gopal.a)











