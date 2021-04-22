#insertion sort
lit=[44,2,83,83,7,100,67,21]
i=0
while i<len(lit):
    res=lit[i]
    j=i-1
    while j>=0 and res<lit[j]:
        lit[j+1],lit[j]=lit[j], lit[j+1]
        print(lit)
        j=j-1      
    else:
        i+=1
        continue
else:
    print("The insertion sort list is  :",lit)
	
#merge sort
n=int(input("Enter the upper list limit :"))
li=[]
for i in range(0,n):
    li.append (int(input("Enter the list :")))
def merge(li):
    if len(li)>1:
        mid=len(li)//2
        left=li[:mid]
        right=li[mid:]
        merge(left)
        merge(right)
        i=0
        j=0
        k=0
        while i<len(left) and j<len(right):
            if left[i]<= right[j]:
               li[k]=left[i]
               i+=1
               k=k+1
            else:
                li[k]=right[j]
                j+=1
                k=k+1
        while i<len(left):
            li[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            li[k]=right[j]
            j+=1
            k+=1
merge(li)
print("The sorted list is",li)
#Quick Sort
a=[10,1,100,5,20,1000,0,1,58,29,1,65,10]
def pivot(a,c,b):
    pivot=a[c]
    i=c+1
    j=b
    while True:
        while i<=j and a[i]<=pivot:
            i+=1
        while i<=j and a[j]>=pivot:
            j-=1
        if i<=j:
            a[j],a[i]=a[i],a[j]
        else: 
            break
    a[j],a[c]=a[c],a[j] 
    return j
def quicksort(a,i,j):
    if i<j:
        cen_value=pivot(a,i,j)
        quicksort(a,i,cen_value-1)
        quicksort(a,cen_value+1,j)
quicksort(a,0,len(a)-1)
print(a)

if i<j:
cen_value=pivot(a,i,j)
quicksort(a,i,cen_value-1)
quicksort(a,cen_value+1,j)
quicksort(a,0,len(a)-1)
print(a)
#selection sort
a=[10,1,50,2,0,2,8,100,2000,3,0,6]
i=0
b=0
j=1
while i<len(a):
    while j<len(a):
        if a[j]<a[i]:
            a[i],a[j]=a[j],a[i]
            j+=1
        else:
            j+=1
    b+=1
    c=b+1
    j=c
    i+=1
print(a)

        
            
