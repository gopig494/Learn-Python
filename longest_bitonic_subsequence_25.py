
bi = [0 , 8 , 4, 12, 2, 10 , 6 , 14 , 2 , 9 , 5 , 13,3, 11 , 7 , 2]

def lbs(bi):
	#find the lenght 
	n = len(bi)
	#longest increasing sequence
	lis = [1 for i in range(n+1)]
	for i in range(1 , n):
		for j in range(0 , i):
			if ((bi[i] > bi[j]) and (lis[i] < lis[j] +1)):
				lis[i] = lis[j] + 1
    #longest decreasing sequence
	lds = [1 for i in range(n+1)]

	for i in reversed(range(n-1)): 
		for j in reversed(range(i-1 ,n)): 
			if (bi[i] > bi[j] and lds[i] < lds[j] + 1):
				lds[i] = lds[j] +1
    # find the maximum value of lis+lds-1 for longest bitonic subsequence
	maximum = 0
	for i in range(0 , n+1):
		maximum = max((lis[i] + lds[i]-1), maximum)
	return maximum
#print and function call
print("Length of LBS is",lbs(bi))

