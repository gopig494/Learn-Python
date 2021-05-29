#Methods of using Functions
#1
def outer():
    def inner(a):
        print("I got decorated",a)
    return inner
a=outer()
a(1)

a=outer()
a

a=outer
a()(1)

outer()('ok')



#1.1
def is_called(s):
    print(s)
    def is_returned(a):
        print("Hello")
        print(a)
    return is_returned('a')


new = is_called(1)  
new

#2
def is_called(s):
    print(s)
    def is_returned(a):
        print("Hello")
        print(a)
    a=10
    return is_returned(a)


new = is_called(1)  
new

#3
def is_called(s):
    print(s)
    def is_returned_1(frst):
        print("i am first function")
        print(a)
    a=10
    b='Gopi'
    def is_returned_2(argu):
        print(argu)
        print("i am sencond function")
   
    return is_returned_1(a),is_returned_2(b)

is_called(1)  

#4
def is_called(s):
    print(s)
    def is_returned_1(frst):
        print("i am first function")
        print(a)
    a=10
    b='Gopi'
    def is_returned_2(argu):
        print(argu)
        print("i am sencond function")
   
    return is_returned_1(a),is_returned_2(b)

ali=is_called(1)  
ali

#5
def is_called(s):
    print(s)
    def is_returned_1(frst):
        print("i am first function")
        print(a)
    a=10
    b='Gopi'
    def is_returned_2(argu):
        print(argu)
        print("i am sencond function")
   
    return is_returned_1(a),is_returned_2(b)

ali=is_called  
ali('alising')

#6
#we can't pass parameter to tuple of function
def is_called(s):
    print(s)
    def is_returned_1(frst):
        print("i am first function")
        print(a)
    a=10
    b='Gopi'
    def is_returned_2(argu):
        print(argu)
        print("i am sencond function")
   
    return is_returned_1,is_returned_2

ali=is_called('alising') 
ali(1)(2)

#7
#we can call functions tuple format 
def outer(b):
    print(b)
    def inner(a):
        print("I got decorated",a)
    return inner
#a=outer(inner)
#a(1)

def is_called(s):
    print(s)
    def is_returned_1(frst):
        print("i am first function")
        print(a)
    a=10
    b='Gopi'
    def is_returned_2(argu):
        print(argu)
        print("i am sencond function")
   
    return is_returned_1

ali=is_called('alising') 
ali(1),outer("i am outer function")

#8
#passing a function as a argument
def outer(func):
    def inner():
        print("I got decorated")
        func()
    return inner

def passfun():
    print("I am ordinary")
   
store = outer(passfun)
store()

#Decorators

#1
def outer(func):
    def inner():
        print("I got decorated")
        func("why do you called me")
    return inner

def passfun(ab):
    print("I am ordinary")
    print(ab)
store = outer(passfun)
store()

#2
def outer(func):
    def inner(ab):
        print(ab)
        print("I got decorated")
        func("why do you called me")
    return inner

def passfun(ab):
    print("I am ordinary")
    print(ab)
store = outer(passfun)
store('inner fun value')

#3
def dec(a):
    def inn(m):
        if m==1:
            print('i am m',1)
        else:
            a(m)
    return inn

@dec        #this is decorator
def dis(m):
    print('outer',m)   #this is equal to 
dis(1)                  #dis=dec(dis)

a=dec(dis)
a(1)

#4
def star(func):
    def inner(a):
        print("*" * 30)
        func(a)
        print("*" * 30)
    return inner


def percent(func):    #here in fun the printer will pass
    def inner(a):
        print("%" * 30)
        func(a)
        print("%" * 30)
    return inner
@star
@percent                #decorator
def printer(msg):
    print(msg)
printer("Hello")


printer=star(printer)   #how the decorator works
printer(1)

printer=percent(printer)
printer(1)

percent(printer)(1)

#5
#you can understand clarly
def star(func):    #here in fun the printer will pass
    def inner(a):  #hello is a argument 
        print((a,",") * 5)
        func(a)   #here the printer function call
    return inner
@star    #decorator
def printer(msg):
    print(msg)
printer("Hello")

print("____________________________________________")

print( )


printer=star(printer)   #1 internal working of decorator
printer('gopi')

print("____________________________________________")

print( )

star(printer)('muthu')   #2 #1 internal working of decorator

