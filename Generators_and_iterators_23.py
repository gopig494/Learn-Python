#Iterators and Generators
#Iterators
#1
li=[10,20,30,40]
tu=50,60,70,80
se={90,100,110,120}
v1=iter(li)
print(next(v1))
print(next(v1))
print(next(v1))
print(next(v1))

#2
li=[10,20,30,40]
tu=50,60,70,80
se={90,100,110,120}
v1=iter(li)
for i in v1:
  print(i)

#3
li=[10,20,30,40]
tu=50,60,70,80
se={90,100,110,120}


v1=iter(li)
v2=iter(tu)
v3=iter(se)

print(next(v1))
print(next(v1))
print(next(v1))
print(next(v1))
  
for i in v2:
  print("li",i)
  
  
for i in v3:
  print("se",i)
  
 
#Iteraors in class

#1
class hey:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

obj=hey()
objvar = iter(obj)

print(next(objvar))
print(next(objvar))
print(next(objvar))
print(next(objvar))
print(next(objvar)) 

#2
class hey:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

obj=hey()
objvar = iter(obj)

for i in objvar:
  print(i)
  
#3
class hey:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    if x==100:
      raise StopIteration
    return x
    
obj=hey()
objvar = iter(obj)

for i in objvar:
  print(i)
  
#4
class hey:
  def __init__(self):
    self.i=500
  def __iter__(self):
    self.a = 1
    return self

  def __next__(obj1):
    x = obj1.i
    obj1.i += 1
    if x==600:
      raise StopIteration
    return x
    

obj=hey()
obj1=hey()

objvar = iter(obj)
for a in objvar:
  print(a)

  
#5
class hey:
  def __init__(self):
    self.i=500
  def __iter__(self):
    self.a = 1
    return self

  def __next__(obj1):
    x = obj1.i
    obj1.i += 1
    if x==100:
      raise StopIteration
    return x
    

obj=hey()
obj1=hey()

objvar = iter(obj)
print(next(objvar))
print(next(objvar))
print(next(objvar))
print(next(objvar))


#Generaotrs
#1
#generator function
# A generator function that yields 1 for first time,
# 2 second time and 3 third time
def genobj():
    yield 1            
    yield 2            
    yield 3            
   
# Driver code to check above generator function
for value in genobj(): 
    print(value)
    
    
# Generator object
def genobj():
    yield 1            
    yield 2            
    yield 3  
var=genobj()
print(next(var))
print(next(var))
print(next(var))

#different usage of yield
#1

def genfun(a,b,c):
    add=a+10
    sub=b-10
    mul=c*10
    yield add,sub,mul
#print(genfun(100,20,10))


for i in genfun(100,20,10):
  print(i)
  
#2

def genfun(a,b,c):
    add=a+10
    sub=b-10
    mul=c*10
    yield add
    yield sub
    yield mul
#print(genfun(100,20,10))

for i in genfun(100,20,10):
  print(i)
  
#generator object

#1

def genfun(a,b,c):
    add=a+10
    sub=b-10
    mul=c*10
    yield add,sub,mul
#print(genfun(100,20,10))
var=genfun(100,20,10)
print(next(var))

for i in genfun(100,20,10):
  print(i)
  
#2

def genfun(a,b,c):
    add=a+10
    sub=b-10
    mul=c*10
    yield add
    yield sub
    yield mul
#print(genfun(100,20,10))
var=genfun(100,20,10)
print(next(var))
print(next(var))
print(next(var))

for i in genfun(100,20,10):
  print(i)
