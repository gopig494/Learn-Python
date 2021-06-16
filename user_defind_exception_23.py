
#1

class abc(Exception):
	def __init__(self,data):
		self.data=data
	
def fun():
	try:
		a=input("Enter Your Age : ")
		if int(a)>5:
			print("You Are Eligible")
			fun()

		else:
			exp=abc(" You Are Not Eligible")
			raise exp
	except abc:
		print("You Are Not Eligible") 
		fun()
fun()	

	
    
#2
def fun():
	a=input("Enter Your Age : ")
	if int(a)>5:
		print("You Are Eligible")
		fun()
	else:
		print("You Are Not Eligible")
		fun()	
fun()	
    
