#Method overloading in oops
#1
class obj:
	def meth(self,*n):
		if len(n)==4:
			a,b,c,d=n
			print('model :',a)
			print('brand :',b)
			print('warrenty :',c)
			print('serviceperiod :',d)
		if len(n)==3:
			a,b,c=n
			print('model :',a)
			print('brand :',b)
			print('warrenty :',c)
		if len(n)==2:
			a,b=n
			print('model :',a)
			print('brand :',b)
		if len(n)==1:
			a=n
			print('model :',a)
		if len(n)==0:
			print("No details Found")
car=obj()
car.meth(2018,'TATA',5,'Every 6 Months Once')
car.meth(2021,'Hundai',2)
car.meth(2005,'Hero')
car.meth()

#Constructor overloading
#1
class obj:
	def __init__(self,*n):
		name,age=n
		self.name=name
		self.age=(age,'Years')
human=obj('gopi',25)
bus=obj('TATA',5)

print(bus.name)
print(bus.age)

print(human.name)
print(human.age)

#2
class obj:
	def __init__(self,*n):
		if len(n)==4:
			a,b,c,d=n
			self.model=a
			self.brand=b
			self.warrenty=c
			self.serviceperiod=d
		if len(n)==3:
			a,b,c=n
			self.model=a
			self.brand=b
			self.warrenty=c
		if len(n)==2:
			a,b=n
			self.model=a
			self.brand=b
		if len(n)==1:
			a=n
			self.model=a

bus=obj(2018,'TATA',5,'Every 6 Months Once')
car =obj(2021,'Hundai',2)
bike=obj(2005,'Hero')

print(bus.model)
print(bus.brand)
print(bus.warrenty)
print(bus.serviceperiod)

#Types Of Variables
#Local variable ( Method level variable ).
#Instance variable ( Object level variable ).
#Static variable ( Class level variable ).

#Local Varibales
#Constructor
class obj:
	def __init__(self,a,b,c,d):
			ac='i am local variable'    #ac,year,brand #local variables
			year=a
			brand=b
			print(year)
			print(brand)
			print(ac)
	
bus=obj(2018,'TATA',5,'Every 6 Months Once')

#method local variable

class obj:
	def meth(self,a,b,c,d):
			ac='i am local variable'
			year=a
			brand=b
			print(year)
			print(brand)
			print(ac)
	
bus=obj()
bus.meth(2018,'TATA',5,'Every 6 Months Once')

#instance variables
#1
class obj:
	def __init__(self,a,b,c,d):  #self denote the instance 
			self.model=a
			self.brand=b
			self.warrenty=c
			self.serviceperiod=d

bus=obj(2018,'TATA',5,'Every 6 Months Once')

print(bus.model)
print(bus.brand)
print(bus.warrenty)
print(bus.serviceperiod)

#2
class obj:
	def __init__(self,a,b,c,d):
			self.model=a
			self.brand=b
			self.warrenty=c
			self.serviceperiod=d

bus=obj(2018,'TATA',5,'Every 6 Months Once')
car=obj(2018,'TATA',5,'Every 6 Months Once')

print(bus.model)
print(bus.brand)
print(bus.warrenty)
print(bus.serviceperiod)

print(car.model)
print(car.brand)
print(car.warrenty)
print(car.serviceperiod)

#3
class obj:
	def __init__(self,a,b,c,d):
			self.model=a
			self.brand=b
			self.warrenty=c
			self.serviceperiod=d
	def meth(self):
		print(self.model)

bus=obj(2018,'TATA',5,'Every 6 Months Once')
car=obj(2018,'TATA',5,'Every 6 Months Once')

bus.meth()
car.meth()

#4
#reassgin the instance variable outside the class
class obj:
	def __init__(self,a,b,c,d):
			self.model=a
			self.brand=b
			self.warrenty=c
			self.serviceperiod=d
	def meth(self):
		print(self.model)
		self.model=1975
		print(self.model)

bus=obj(2018,'TATA',5,'Every 6 Months Once')
car=obj(2018,'TATA',5,'Every 6 Months Once')

print(bus.model)
bus.model=1998
print(bus.model)
bus.meth()
print(bus.mosel)

#Declare instance variables inside the class of method 

class obj:
	def __init__(self,a,b,c,d):
			self.model=a
			self.brand=b
			self.warrenty=c
			self.serviceperiod=d
	def meth(self):
		self.month='jan'

bus=obj(2018,'TATA',5,'Every 6 Months Once')
car=obj(2018,'TATA',5,'Every 6 Months Once')

#print(bus.month)
bus.meth()
print(bus.month)

#	Static variable
#1
class st:
	a=10
	def __init__(self,name):
		self.name=name
	def fun(self):
		print(self.name)
		print(self.a)
obj=st("gopi")

print(obj.name)
obj.fun()
print(obj.a)
print(st.a)

#2
class st:
	a=10
	def __init__(self,name):
		self.name=name
	def fun(self):
		print(self.name)
		print(self.a)
obj=st("gopi")
st.a=100  #note the reassignment
print(obj.name)
obj.fun()
print(obj.a)
print(st.a)

#3
class st:
	a=10
	def __init__(self,name):
		self.name=name
	def fun(self):
		print(self.name)
		print(self.a)
obj=st("gopi")
obj.a=100  #note the reassignment
print(obj.name)
obj.fun()
print(obj.a)
print(st.a)

#4
class st:
	a=10
	def __init__(self,name):
		self.name=name
	def fun(self):
		st.a='five Hundred'   #note the reassignment
		print(self.name)
		print(self.a)
obj=st("gopi")
obj.a=100  #note the reassignment
print(obj.name)
obj.fun()
print(obj.a)
print(st.a)





