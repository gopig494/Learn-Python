#split and Reverse a String
#1
intp="gopi python java india" 
l=intp.split()
j=0
li=[]
for i in range(1,len(l),2):
	ab=l[j]
	j+=2
	li.append(ab)
	bc=l[i]
	li.append(bc[::-1])
print(li)

#2
intp="gopi python java india" 
l=intp.split()
j=0
li=[]
while j<len(l):
	if j%2!=0:
		a=l[j]
		li.append(a[::-1])
		j+=1
	else:
		b=l[j]
		li.append(b)
		j+=1
else:
	print(li)
	
#join() and Split()

intp="gopi python java india" 
l=intp.split()
j=0
li=[]
while j<len(l):
	if j%2!=0:
		li.append(l[j][::-1])
		j+=1
	else:
		li.append(l[j])
		j+=1
else:
	out=" ".join(li)
	print(out)
	
#By using Reverse() and split() and join()
#1
#while loop
intp="gopi python java india" 
l=intp.split()
j=0
li=[]
while j<len(l):
	if j%2!=0:
		a=list(l[j])
		a.reverse()
		li.append(a)
		j+=1		
	else:
		li.append(l[j])
		j+=1
else:
	i=0
	while i<len(li):
		if i%2!=0:
			out="".join(li[i])
			li[i]=out
			i+=1
		else:
			i+=1
	else:
		res=" ".join(li)
		print(res)
#2 #for loop
new=[]  
intp="gopi python java india" 
name=intp.split()
for i in range(len(name)):
    if i%2==0:
        new.append(name[i])
    else:
        rev=list(name[i])
        rev.reverse()
        new.append("".join(rev))
else:
    print(" ".join(new))
	



