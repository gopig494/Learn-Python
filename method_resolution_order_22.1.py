#You can Clearly Understand by Following Program
#mro #Method order resoltion in python
#output
#Class I-1
#Class E-2
#Class C-3
#Class D-4
#Class A-5
#Class H-6
#Class F-7
#Class G-8
#Class B-9


#1

class A:
  pass
   
class B:
  def mobile(self):
    print('Class B')

class C(A):
  pass
    
class D(A):
  pass
 
class E(C,D):
  pass

class F(B):
  pass    
    
class G(B):
  pass
    
class H(F,G):
 pass
    
class I(E,H):
  def mobile(self):
    print('Class I')
   
    
obj=I()
obj.mobile()

#2
class A:
  def mobile(self):
    print('Class A')
   
class B:
  def mobile(self):
    print('Class B')

class C(A):
  def mobile(self):
    print('Class C')
    
class D(A):
  pass
 
class E(C,D):
  def mobile(self):
    print('Class E')

class F(B):
  pass    
    
class G(B):
  pass
    
class H(F,G):
 pass
    
class I(E,H):
  pass
   
    
obj=I()
obj.mobile()

#3
class A:
  def mobile(self):
    print('Class A')
   
class B:
  def mobile(self):
    print('Class B')

class C(A):
  def mobile(self):
    print('Class C')
    
class D(A):
  pass
 
class E(C,D):
  pass

class F(B):
  pass    
    
class G(B):
  pass
    
class H(F,G):
 pass
    
class I(E,H):
  pass
   
    
obj=I()
obj.mobile()


#4
class A:
  def mobile(self):
    print('Class A')
   
class B:
  def mobile(self):
    print('Class B')

class C(A):
  pass
    
class D(A):
  def mobile(self):
    print('Class D')
 
class E(C,D):
  pass

class F(B):
  pass   
    
class G(B):
  pass
    
class H(F,G):
 pass
    
class I(E,H):
  pass

obj=I()
obj.mobile()

   
    
#5
class A:
  def mobile(self):
    print('Class A')
   
class B:
  def mobile(self):
    print('Class B')

class C(A):
  pass
    
class D(A):
  pass
 
class E(C,D):
  pass

class F(B):
  pass    
    
class G(B):
  pass
    
class H(F,G):
 pass
    
class I(E,H):
  pass
   
obj=I()
obj.mobile()

#6

class A:
  pass
   
class B:
  def mobile(self):
    print('Class B')

class C(A):
  pass
    
class D(A):
  pass
 
class E(C,D):
  pass

class F(B):
  pass    
    
class G(B):
  pass
    
class H(F,G):
 def mobile(self):
    print('Class H')
    
class I(E,H):
  pass
   
    
obj=I()
obj.mobile()



#7
class A:
  pass
   
class B:
  def mobile(self):
    print('Class B')

class C(A):
  pass
    
class D(A):
  pass
 
class E(C,D):
  pass

class F(B):
  def mobile(self):
    print('Class F')    
    
class G(B):
  pass
    
class H(F,G):
 pass
    
class I(E,H):
  pass
   
    
obj=I()
obj.mobile()


#8

class A:
  pass
   
class B:
  def mobile(self):
    print('Class B')

class C(A):
  pass
    
class D(A):
  pass
 
class E(C,D):
  pass

class F(B):
  pass   
    
class G(B):
  def mobile(self):
    print('Class G')
    
class H(F,G):
 pass
    
class I(E,H):
  pass
   
    
obj=I()
obj.mobile()



#9
class A:
  pass
   
class B:
  def mobile(self):
    print('Class B')

class C(A):
  pass
    
class D(A):
  pass
 
class E(C,D):
  pass

class F(B):
  pass   
    
class G(B):
  pass
    
class H(F,G):
 pass
    
class I(E,H):
  pass
   
    
obj=I()
obj.mobile()





