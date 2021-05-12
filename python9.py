#Opps #Creating class #creating object #creating attributes and behavior of an object
class market:
	brand='redmi'
	model='note 8 pro'
	ram='8 gb'
	 
	def behavior(self,b,c):
		calculate=b+c
		return calculate
mobile=market()
print(mobile.brand)
print(mobile.model)
print(mobile.ram)
print(mobile.behavior(1,10))

#using a attributes and behaviors for 2 objects
class market:
	name='redmi'
	model='note 8 pro'
	ram='8 gb' 
	def behavior(self,b,c):
		calculate=b+c
		return calculate
mobile=market() #object 1
tv=market()  #object 2
#object 1
print(mobile.brand)
print(mobile.model)
print(mobile.ram)
print(mobile.behavior(1,10))

#object 2
print(tv.brand)
print(tv.model)
print(tv.ram)
print(tv.behavior(1,10))

#Constructor
#1
class market:
	def __init__(self,brand,model,ram):
		self.brand=brand
		self.model=model
		self.ram=ram
mobile=market('redmi','note 8 pro','8gb')
print(mobile.brand)

#2
class market:
	def __init__(self,a,b,c):
		self.brand=a
		self.model=b
		self.ram=c
mobile=market('redmi','note 8 pro','8gb')
print(mobile.brand)
		
#Method inside the class
#1
class market:
	def __init__(self,a,b,c):
		self.brand=a
		self.model=b
		self.ram=c
	def behavior(self):
		return self.model, self.brand, self.ram
mobile=market('redmi','note 8 pro','8gb')
print(mobile.behavior())
	
#2
class market:
	def __init__(self,a,b,c):
		self.brand=a
		self.model=b
		self.ram=c
	def behavior(self,m,l):
		return m*l, self.model, self.brand, self.ram
mobile=market('redmi','note 8 pro','8gb')
print(mobile.behavior(10,100))
		
#3
class market:
	def __init__(self,a,b,c):
		self.brand=a
		self.model=b
		self.ram=c
	def behavior(self):
		return "{} - {} - {}".format(self.brand,self.model,self.ram)
mobile=market('redmi','note 8 pro','8gb')
print(mobile.behavior())

#Destructor
# Python program to illustrate destructor
class Employee: 
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print('Employee created')
    def __del__(self):
        print("Destructor called") 
def Create_obj():
    print('Making Object')
    obj = Employee(10,20)
    print('function end')
    return obj
  
print('Calling Create_obj() function...')
obj = Create_obj()
print('Program End')
print(obj.a)

#Inheritance
#1
class Bird:  # parent class
    def __init__(self):
        self.name='indian'
        self.age='55'
        print("Bird is ready")
    def whoisThis(self):
        print("Bird")
    def swim(self):
        print("Swim faster")
    def fly(self):
        print("fly faster")
class Penguin(Bird): # child class
    def __init__(self):
        super().__init__()
        print("Penguin is ready")
    def whoisThis(self):
        print("Penguin")
    def run(self):
        print("Run faster")
obj=Penguin()
obj.fly()
obj.run()
obj.whoisThis()

#2
class Bird:    # parent class
    def __init__(self):
        self.name='indian'
        self.age='55'
        print("Bird is ready")
    def whoisThis(self):
        print("Bird")
    def swim(self):
        print("Swim faster")
    def fly(self):
        print("fly faster")
class Penguin(Bird):    # child class
	pass
obj=Penguin()
obj.fly()
obj.whoisThis()

#Encapsulation
#With Encapsulation
class market:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

mobile = market()
mobile.sell()

	# change the price
mobile.__maxprice = 1000
mobile.sell()

	# using function to change the price
mobile.setMaxPrice(1000)
mobile.sell()

#2
#without encapsulation
class market:

    def __init__(self):
        self.maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.maxprice))
mobile = market()
mobile.sell()

	# change the price
mobile.maxprice = 1000
mobile.sell()


#Polymorphism

class Parrot:
    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can't swim")

class Penguin:
    def fly(self):
        print("Penguin can't fly")
    
    def swim(self):
        print("Penguin can swim")

		# common interface
def flying_test(bird):
    bird.fly()
blu = Parrot()
peggy = Penguin()
flying_test(blu)
flying_test(peggy)
		
		
		
		
		
		
		
		
		