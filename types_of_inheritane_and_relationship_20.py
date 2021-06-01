#Types of inheritance and relationships in oops 

#Types of inheriteance 
#Single Inheritance
class parent:
	def __init__(self):
		self.name='parent'
	def fun(self):
		print('i am parent class')
pobj=parent()

class child(parent):
	def fun1(self):
		print('i am parent child')

cobj=child()

print(cobj.name)

#multiple inheritance
class parent1:
	def p1(self):
		print("i am parent1 class")
p1obj=parent1()

class parent2:
	def __init__(self):
		self.name='parent2'
	def fun(self):
		print('i am parent2 class')
p2obj=parent2()

class child(parent1,parent2):
	def fun1(self):
		print('i am parent child')

cobj=child()


cobj.p1()
cobj.fun()
cobj.fun1()

#multilevel inheritance


class parent:
	def p1(self):
		print("i am parent class")
pobj=parent()

class child1(parent):
	def __init__(self):
		self.name='child1'
	def fun(self):
		print('i am child1 class')
c2obj=child1()

class child2(child1):
	def fun1(self):
		print('i am child2')

c2obj=child2()


c2obj.p1()
c2obj.fun()
c2obj.fun1()

#Hierarchical Inheritance.
class parent:
	def p1(self):
		print("i am parent class")
pobj=parent()

class child1(parent):
	def __init__(self):
		self.name='child1'
	def fun(self):
		print('i am child1 class')
c1obj=child1()

class child2(parent):
	def fun1(self):
		print('i am child2')

c2obj=child2()


class child3(parent):
	def fun2(self):
		print('i am child3')
	
c3obj=child3()


c1obj.p1()
c2obj.p1()
c3obj.p1()

#Hybrid Inheritance.

class parent:
	def p1(self):
		print("i am parent class")
pobj=parent()

class parent1:
	def p2(self):
		print("i am parent class")
p1obj=parent1()

class child1(parent):
	def __init__(self):
		self.name='child1'
	def fun(self):
		print('i am child1 class')
c1obj=child1()

class child2(child1,parent1):
	def fun1(self):
		print('i am child2')

c2obj=child2()


class child3(child2):
	def fun2(self):
		print('i am child3')
	
c3obj=child3()


c3obj.p1()
c3obj.p2()
c3obj.fun()
c3obj.fun1()
c3obj.fun2()

#HAS-A Relationship
class whatsapp:
	colour="Green"
	def __init__(self,a,b):
		self.message=a
		self.name=b
	def obj(self,a,b):
		print("i am instance method")
	@staticmethod
	def st():
		print("i am static method")
	@classmethod
	def cl(cls):
		print("i  am class method")
wobj=whatsapp(100,200)
		
class android:
	colour="Blue"
	def __init__(self,a,b):
		self.app=whatsapp('hello','GOPI')
		self.message=a
	def obj(self,a,b):
		print("i am instance method")
	@staticmethod
	def st():
		print("i am static method")
	@classmethod
	def cl(cls):
		print("i  am class method")
	
MI=android('hi',1)

print(MI.app.message)
print(MI.app.colour)
MI.app.st()
(MI.colour)
MI.app.obj(1,2)
MI.app.cl()
print(MI.message)


