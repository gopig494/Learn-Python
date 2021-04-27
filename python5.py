#Tuple Denotion

t=10,20,30,40
print(type(t))

t1=10,
print(type(t))

t2=(10,20,30,40)
print(type(t))

#Empty Tuple
t=()

#Convert list into Tuple
l=[10,20,30,40,50]
t=tuple(l)
print(t)

#Using Range()
t=tuple(range(10))
print(t)

#Tuple is Immutable
l=(10,20,30,40,50)
l[0]=10
print(l)

#Mathematical Operations in Tuple
#1
l=(10,20,30,40,50)
l1=(50,60,70,200)
a=l+l1
print(a)

#2
l=(10,20,30,40,50)
l1=(50,60,70,200)
a=10*l1
print(a)

#Tuple() Functions
#count()
l=(10,20,30,40,50,10,10)
le=len(l)
a=le*l
b=a.count(10)
print(b)

#immutable

l=(10,20,30,40,50,10,10)
print(id(l))
le=len(l)
l=le*l
print(id(l))
b=l.count(10)
print(b)

#Sorting()
#1
l=(100,20,30,40,50,1000,10)
print(sorted(l)
	  
#2	  
l=(100,20,30,40,50,1000,10)
print(sorted(l,reverse=True))
	  
#3
l=(100,20,30,40,50,1000,10)
print(min(l))
print(max(l))
print(sum(l))
	  
#Tuple packing and unpacking
#packing
t=10,30,50,60,100
	  
#tuple unpacking
p,q,r,s,t=t
print(p)
print(q)
print(r)
print(s)
print(t)
	  
#Tuple Comprehension
#1
t=(i for i in range (10))
print(type(t))
	  
#2
t=(i for i in range (10))
print(tuple(t))
