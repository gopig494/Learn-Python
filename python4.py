#Convert list into set

l=[10,10,20,30,40,50,50]
s=set(l)
print(s)

#convert string to set
a='abcd a'
s=set(a)
print(s)

#creating empty set
s=set()

#add()
l={10,10,20,30,40,50,50}
l.add(1000)
print(l)

#update()
#1
s={10,10,20,30,40,50,50}
l=[100,200,300,300,300,300]
m="gopi gokul"
s.update(l)
print(s)
s.update(m)
print(s)

#2
s={10,10,20,30,40,50,50}
l=[100,200,300,300,300,300]
m="gopi gokul"
s.update(l,m,range(0,20))
print(s)

#Mathematics Operations in set
#1
s={10,20,30,40,50}
l={50,10,100,200,60}
print(s.union(l))
print(s.intersection(l))
print(s.difference(l))
print(s.symmetric_difference(l))

#2
s={10,20,30,40,50}
l={50,10,100,200,60}
print(s|l)
print(s&l)
print(s-l)
print(s^l)

#copy()
s={10,20,30,40,50}
s1=s.copy()
print(s1)

#pop()
s={10,20,30,40,50}
s.pop()
print(s)

#remove
s={10,20,30,40,50}
s.remove(50)
print(s)

#remove vs discard

s={10,20,30,40,50}
s.remove(500)
print(s)

s={10,20,30,40,50}
s.discard(500)
print(s)

#clear
s={10,20,30,40,50}
s.clear()
print(s)

#set comprehension
#1
s={sl for sl in range(10)}
print(s)

#2
l=10,20,30,40,50
s={sl for sl in l}
print(s)

#how dupicates removed in set
#List Ex:
l=[10,10,20,30,20,40,50]
l1=[]
for i in l:
	if i not in l1:
		l1.append(i)
else:
	print(l1)
	
#2
l=10,10,20,30,20,40,50
l1=set()
for i in l:
	if i not in l1:
		l1.add(i)
else:
	print(l1)
	
#Set Mutable and Immutable 
#1 set is mutable when not using the frozenset function
l={'apple','orange','banana',20.0,20,True}
print(id(l))
l.add(500)
print(id(l))

#set is immutable when using the frozenset function
l2=frozenset(l)
print(id(l2))
l2.add(500)
print(id(l2))

