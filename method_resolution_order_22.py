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
  def mobile(self):
    print('Class A')
    
class B:
  def mobile(self):
    print('Class A')
    
class C(A):
  def mobile(self):
    print('Class C')
    
class D(A):
  def mobile(self):
    print('Class D')
 
class E(C,D):
  def mobile(self):
    print('Class E')

class I(E):
  def mobile(self):
    print('Class I')
   
class F(B):
  pass    
    
class G(B):
  def mobile(self):
    print('Class G')
    
class H(F,G):
 pass
    
class I(H):
  pass
    
    
obj=I()
obj.mobile()


    
    

 
 
