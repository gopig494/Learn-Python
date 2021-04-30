#Copy the dictionary
#1
dic={'colour':'black',
'place':'salem',
'name':'gopi'}
dic1=dic
print(dic1)
#2
dic={'colour':'black',
'place':'salem',
'name':'gopi'}
dic1=dic.copy()
print(dic1)

#setdefault()
dic={'colour':'black',
'place':'salem',
'name':'gopi'}
dic1=dic.setdefault(1,2)
print(dic)
print(dic1)

#2
dic={'colour':'black',
'place':'salem',
'name':'gopi'}
dic1=dic.setdefault('colour',2)
print(dic)
print(dic1)

#get()
#1
dic={'colour':'black',
'place':'salem',
'name':'gopi'}
dic1=dic.get('colour')
print(dic1)

#2
dic={'colour':'black',
'place':'salem',
'name':'gopi'}
dic1=dic.get(100)
print(dic1)

#3
dic={'colour':'black',
'place':'salem',
'name':'gopi'}
dic1=dic.get(100,'not stored in dicitionary')
print(dic1)

#Find how many time a character present in a given input 
#Dictionary Format
c=input("Enter the characters  :")
d={}
for j in c:
	d[j]=d.get(j,0)+1
else:
	print(d)
#2
c=input("Enter the characters  :")
d={}
for j in c:
	d[j]=d.get(j,0)+1
else:
	for i in d.items():
		print(i)
		
#3
c=input("Enter the characters  :")
d={}
for j in c:
	d[j]=d.get(j,0)+1
else:
	for i,j in d.items():
		print(i,"present in ",end='-')
		print(j," Times")
		
#Print Only the duplicates
c=input("Enter the characters  :")
d={}
for j in c:
	d[j]=d.get(j,0)+1
else:
	for i,j in d.items():
		if j>1:
			print(i,"present in ",end='-')
			print(j," Times")
			
#ignore the duplicates
c=input("Enter the characters  :")
d={}
for j in c:
	d[j]=d.get(j,0)+1
else:
	for i,j in d.items():
		if j==1:
			print(i,"present in ",end='-')
			print(j," Times")
#Print the  how many time a character present in a given input
#Assending order
c=input("Enter the characters  :")
d={}
for j in c:
	d[j]=d.get(j,0)+1
else:
	for i,j in sorted(d.items()):
		print(i,"present in ",end='-')
		print(j," Times")
		
#Find how many time a object present in a given list
l=[100,200,300,100,100,500,200,300]
d={}
for i in l:
	d[i]=d.get(i,0)+1
else:
	for j in d:
		print(j,"present in" ,d[j], 'times')

#practice program 
#increasing 10 % of the values
d={'apple':100,'orange':50,'banana':30}
for i in d:
	d[i]=d[i]+d[i]/100*10
print(d)

#swapping keys and values
#The values must be not containing duplicates
#1
d={'apple':100,'orange':50,'banana':30}
c={}
for i in d:
	a=d[i]
	b=i
	c[a]=b
else:
	print(c)

#2
d={'apple':100,'orange':50,'banana':30}
c={}
for i,j in d.items():
	c[j]=i
print(c)
	
#Dictionary Comprehensions
d={i:i+1 for i in range(10)}
print(d)

#Changing keys into values and values into keys
#1
d={'apple':100,'orange':50,'banana':30}
c={i:j for j,i in d.items()}
print(c)

#2
d={'apple':100,'orange':50,'banana':30}
d={i:j for j,i in d.items()}
print(d)

#Practice Programs
#1
d={'apple':100,'orange':50,'banana':30}
for i,j in d.items():
	if j>30:
		print(i,j)
	
#2
d={'zen':10000,'apple':100000,'xiomi':25000,'lenovo':35000}
c={}
for i,j in sorted(d.items()):
	c[i]=j
print(c)

#Sorting a values and arange the values into Correct key
d={'apple':100,'orange':50,'banana':30}
c={}
v={}
for i,j in d.items():
	c[j]=i
else:
	for l,m in sorted(c.items()):
		v[m]=l
	else:
		print(v)

   
	
