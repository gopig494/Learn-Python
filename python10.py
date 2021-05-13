#Oops
#1
#operator overloading
class school:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(s1,s2):
        m1=s1.a+s2.a
        m2=s1.b+s2.b
        s3=school(m1,m2)
        return s3
  
s1=school(100,99)
s2=school(50,60)
s3=s1+s2
print(s3.a)
print(s3.b)

#2
class school:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(s1,s2):
        m1=s1.a+s2.a
        m2=s1.b+s2.b
        s3=m1+m2
        return s3
  
s1=school(100,99)
s2=school(50,60)
s3=s1+s2
print(s3)

#3
class school:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(s1,s2):
        m1=s1.a+s2.a
        m2=s1.b+s2.b
        s3=m1+m2
        return s3
    def __str__(self):
        return 'self.a=100, self.b=99'
  
s1=school(100,99)
s2=school(50,60)
print(s1)

#4
class school:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(s1,s2):
        m1=s1.a+s2.a
        m2=s1.b+s2.b
        s3=m1+m2
        print(s3)
    def __str__(self):
        return 'self.a=100, self.b=99'
  
s1=school(100,99)
s2=school(50,60)
s1+s2
