#super().__init__()
#mro #Method order resoltion in python
#1

class Computer():
    def __init__(self, computer, ram, storage):
        self.computer = computer
        self.ram = ram
        self.storage = storage

# Class Mobile inherits Computer
class Mobile(Computer):
    def __init__(self, computer, ram, storage, model):
        super().__init__("mi", ram, storage)
        self.model = model

Apple = Mobile('Apple', 2, 64, 'iPhone X')
print(Apple.computer)

#2

class Computer():
    def __init__(self, computer, ram, storage):
        self.computer = computer
        self.ram = ram
        self.storage = storage
Xiomi=Computer('MI','8GB','1DB')

# Class Mobile inherits Computer
class Mobile(Computer):
    def __init__(self, computer, ram, storage, model):
        super().__init__(computer, ram, storage)
        self.computer = computer
        self.ram = ram
        self.storage = storage
        self.model = model

Apple = Mobile('Apple', 2, 64, 'iPhone X')
print(Apple.computer)


#MRO
class A:
  def mro(self):
    print('Class A')
    
class B:
 pass
    
    
class D(B):
  pass
    
    
class C(A):
  pass 

class E(D,C):
  pass
    
obj=E()

obj.mro()


    
    

 
 
