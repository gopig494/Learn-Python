#Exception Handling
#1
a=int(input('Enter the number')) #1
b=int(input('Enter the number'))  #0
print(a/b)  #Exception 'zerodivisionerror'

#2
#mini project useing exception handling
import datetime
choose='y'
while choose.upper()=='Y':
    userdata = input('Please Enter Your DOB (dd/mm/yyyy) :')
    try:
        birthday = datetime.datetime.strptime(userdata,'%d/%m/%Y').date()
        #print(birthday)
    except ValueError:
        print("You entered wrong date or wrong format ,Please enter correct format dd/mm/yyy")
        continue 
    currentDate = datetime.date.today()
    #print(currentDate)
    days =currentDate - birthday
    #print(type(days))
    inte=days.days
    #print(type(int))
    if inte > 1830:
        print("You Can Take a Aadhaar With Bio-Metric Data")
    else:
        print("You Can't Take a Aadhaar With Bio-Metric Data")
    while True:
        ch=input("Enter Y to continue and N to Exit:")
        if ch.upper()=='Y' or ch.upper()=='N':
            choose=ch
            break
        else:
            print("Please Enter The Correct Choose  :")
            continue
        
#3
def f():
	try:
		a=int(input("Enter the number 1   :"))
		b=int(input("Enter the number 2   :"))
		print(a+b)	
	except:
		print("You Entered wrong data")
		print("Please Enter Correct data ")
		f()
f()

#4
while True:
	try:
		a=int(input("Enter the number 1:"))
	except ValueError:
		print("Please Enter The Correct Data:")
		continue
	while True:
		try:
			b=int(input("Enter the number 2:"))
		except ValueError:
			print("Please Enter The Correct Data:")
			continue 
		break
	print(a+b)
	break

	
