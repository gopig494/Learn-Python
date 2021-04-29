#Creating Dictionary
#1
dic={}
print(type(dic))

#2
dic=dict()
print(type(dic))

#3
d=dict([(1,1),(2,5)])
print(d)

#Adding key and values in Empty Dictionary
#1
dic={}
dic['fruit']='apple'
print(dic)
#2
dic={'fruits':'apple',
	 'place':'salem',
	 'name':'gopi'
}
print(dic)

#Storing List as a value in Dictionary
dic={'fruits':['apple','orange','banana'],
	 'place':'salem',
	 'name':'gopi'
}
print(dic)

#storing tuple as a key in dictionary
dic={(10,20,30,41,50,100):['apple','orange','banana'],
	 'place':'salem',
	 'name':'gopi'
}
print(dic)

#Printing the dictionary of each list values by tuple key
dic={(10,20,30,41,50,100):['apple','orange','banana'],
	 'place':'salem',
	 'name':'gopi'
}
print(dic[(10,20,30,41,50,100)][0])
#changing the values
dic={(10,20,30,41,50,100):['apple','orange','banana'],
	 'place':'salem',
	 'name':'gopi'
}
dic[(10,20,30,41,50,100)][0]='gopi'
print(dic)
#variable Assignment
#1
i=(10,20,30,40,50)
dic={i:['apple','orange','banana'],
	 'place':'salem',
	 'name':'gopi'
}
dic[i][0]='gopi'
print(dic)

#2
i=(10,20,30,40,50)
j=['apple','orange','banana']
dic={i:j,
	 'place':'salem',
	 'name':'gopi'
}
print(dic)

#Can't use list as a Key Example
i=(10,20,30,40,50)
j=['apple','orange','banana']
dic={j:i,
	 'place':'salem',
	 'name':'gopi'
}
#Use set as a value 
i=(10,20,30,40,50)
j={'apple','orange','banana'}
dic={i:j,
	 'place':'salem',
	 'name':'gopi'
}
print(dic)

#while using set as a value we can't assign a set elelments
i=(10,20,30,40,50)
j={'apple','orange','banana'}
dic={i:j,
	 'place':'salem',
	 'name':'gopi'
}
dic[i][2]='python'
print(dic)

#can't use set as a key
i=(10,20,30,40,50)
j={'apple','orange','banana'}
dic={j:i,
	 'place':'salem',
	 'name':'gopi'
}
print(dic)

#can't use dictionary as a key bacause dicitonary is mutable
i=(10,20,30,40,50)
j={'apple','orange','banana'}
dic={i:j,
	 'place':'salem',
	 'name':'gopi'
}
d={dic:1}
print(d)

#use dictionary as a key
i=(10,20,30,40,50)
j={'apple','orange','banana'}
dic={i:j,
	 'place':'salem',
	 'name':'gopi'
}
d={1:dic}
print(d)

#2 #Nested dictionary item assignment 
i=(10,20,30,40,50)
j=['apple','orange','banana']
dic={i:j,
	 'place':'salem',
	 'name':'gopi'
}
d={1:dic}
d[1][i][2]=1000
print(d)

#3
i=(10,20,30,40,50)
j=['apple','orange','banana']
dic={i:j,
	 'place':'salem',
	 'name':'gopi'
}
d={1:dic}
d[1][i][2]=1000
d[1][i][1]=1
d[1][i][0]=555
print(d)

#we can use Tuple as a value 
i=(10,20,30,40,50)
dic={i:i,
	 'place':'salem',
	 'name':'gopi'
}
print(dic)

#what happen when we will give a key which is not in dictionary
dic={10:20,
	 'place':'salem',
	 'name':'gopi'
}
print(dic[100])

#Receiving input from user for Dictionary 
#While loop
dic={}
m='y'
while m.upper()=='Y':
	a=eval(input("Enter the key  :"))
	b=eval(input("Enter the value :"))
	dic[a]=b
	c=input("Press Y to add more and Press N to finish  :")
	if c.upper()=="Y":
		m=c
	elif c.upper()=="N":
		m=c
	else:
		while c.upper() !="Y" and c.upper() !="N":
			t=input("Enter the correct choose  :")
			if t.upper()=="Y":
				c=t
				m=t
			elif t.upper()=="N":
				c=t
				m=t
			else:
				continue
else:
	print(dic)
#Printing Dictionary by using For loop
#1
i=(10,20,30,40,50)
dic={i:i,
	 'place':'salem',
	 'name':'gopi'
}
for l in dic:
	print(type(l))
	print(l)
#2
i=(10,20,30,40,50)
dic={i:i,
	 'place':'salem',
	 'name':'gopi'
}
for l in dic:
	print(type(l),":",type(dic[l]))
	print(l,":",dic[l])
			
# The key starts with 'i' and ends with 'i'
dic={'colour':'black',
	 'place':'salem',
	 'name':'gopi'}
for l in dic:
	k=l
	if dic[k][0]=='i':
		print(k,":",dic[k])
	elif dic[k][-1]=='i':
		print(k,":",dic[k])
			  
#2
dic={'colour':'black',
	 'place':'salem',
	 'name':'gopi'}
for l in dic:
	k=dic[l]
	if k[0]=='i':
		print(l,":",k)
	elif k[-1]=='i':
		print(l,":",k)
		
#Delete a pair in Dictionary
dic={'colour':'black',
	 'place':'salem',
	 'name':'gopi'}
del dic["colour"]
print(dic)

#Clear the diconary 
dic={'colour':'black',
	 'place':'salem',
	 'name':'gopi'}
dic.clear()
print(dic)

#Delete the Dictionary 
dic={'colour':'black',
	 'place':'salem',
	 'name':'gopi'}
del dic

#Functions
#1
dic={'colour':'black',
	 'place':'salem',
	 'name':'gopi'}
print(len(dic))

#2
dic={'colour':'black',
	 'place':'salem',
	 'name':'gopi'}
print(dic["colour"])
print(dic.get("colour"))

#3
dic={'colour':'black',
	 'place':'salem',
	 'name':'gopi'}
print(dic["colour"])
print(dic.get(123))

#4
dic={'colour':'black',
	 'place':'salem',
	 'name':'gopi'}
dic.pop("colour")
print(dic)

#5
dic={'colour':'black',
	 'place':'salem',
	 'name':'gopi'}
print(dic.pop("colour"))

#6
dic={'colour':'black',
	 'place':'salem',
	 'name':'gopi'}
print(dic.pop("g"))


#7
dic={'colour':'black',
	 'place':'salem',
	 'name':'gopi'}
print(dic.popitem())

#8
dic={'colour':'black',
	 'place':'salem',
	 'name':'gopi'}
print(dic.keys())
print(dic.values())

#9
dic={'colour':'black',
	 'place':'salem',
	 'name':'gopi'}
print(dic.items())

#Printing valus alone
dic={'colour':'black',
	 'place':'salem',
	 'name':'gopi'}
a=dic.values()
for i in a:
	print(i)

#printing keys alone
dic={'colour':'black',
	 'place':'salem',
	 'name':'gopi'}
a=dic.keys()
for i in a:
	print(i)

#Printing keys and values Pair
dic={'colour':'black',
	 'place':'salem',
	 'name':'gopi'}
a=dic.items()
for i in a:
	print(i)







			  