
#oops functions
#Access attributes and methods by using class
class bb:
	b=2
	def bb(self):
		print(a.b)
print(bb().b)
print(bb().bb())

#Access, delete ,identyfy attributes by using functions
class test:
	Mark=2
	RequiredMark=35
	def bb(self):
		print(a.b)
a=test()
print(getattr(a,'Mark'))
print(getattr(a,'RequiredMark'))
print(hasattr(a,'Result'))
setattr(a,'Result','Fail')
print(getattr(a,'Result'))
print(hasattr(a,'Result'))
delattr(a,'Result')
print(hasattr(a,'Result'))
