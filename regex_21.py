#regex #regular expression
#meta characters
#search
import re 

print(re.compile(r'\d\d\d\d\d\d\d\d\d\d').search('9000000049'))


#1
  #method 1
strr=re.compile(r'\d\d\d\d\d\d\d\d\d\d')
res=strr.search('9000000049')

print(res)

  #method 2
res='9000000049'
strr=re.search(r'\d\d\d\d\d\d\d\d\d\d',res)

print(strr)	
 
	#1
res='hi my number is 9000'
strr=re.search(r'\d\d\d\d\d\d\d\d\d\d',res)

print(strr)	

	#2
import re

res='hi my number is 9000000000'
strr=re.search(r'\d{10}',res)

print(strr)	



#2
strr=re.compile(r'\d{10}')
res=strr.search('9000000049')
print(res)

#3
import re 
var='This is my number 9000000049 and 9330000049'
def fun(no):
	stru=re.compile(r'\d{10}')
	res=stru.search(no)
	return res
res=fun(var)
print(res)
if res:
	print (True)
else:
	Print (False)
	
#4
import re 
var='This is my number 916234569871 and 7894561230'
def fun(no):
	stru=re.compile(r'(91)[6-9][0-9]{9}')
	res=stru.search(no)
	return res
res=fun(var)
print(res)
if res:
	print (True)
else:
	print (False)

#5
import re 
var='This is my number 9162345-69871 and 7894561230'
def fun(no):
	stru=re.compile(r'(91)[6-9][0-9]{4}-[0-9]{5}')
	res=stru.search(no)
	return res
res=fun(var)
print(res.group())

#6
#groups
import re 
var='This is my number 9162345-69871 and 7894561230'
def fun(no):
	stru=re.compile(r'(91)([6-9])([0-9]{4})-([0-9]{5})')
	res=stru.search(no)
	print(res.groups())
fun(var)

#group	
import re 
var='This is my number 9162345-69871 and 7894561230'
def fun(no):
	stru=re.compile(r'(91)([6-9])([0-9]{4})-([0-9]{5})')
	res=stru.search(no)
	print(res.group())
fun(var)


#match
#1
import re

strr=re.compile(r'\d\d\d\d\d\d\d\d\d\d')
res=strr.match('9000000049')

print(res)


res='9000000049'
strr=re.match(r'\d\d\d\d\d\d\d\d\d\d',res)

print(strr)	

#2
import re

strr=re.compile(r'\d\d\d\d\d\d\d\d\d\d')
res=strr.match('This is my number 9000000049')

print(res)

if res:
	print("match found")
else:
	print("NO match found")


res='i own this number 9000000049'
strr=re.match(r'\d\d\d\d\d\d\d\d\d\d',res)

print(strr)	

if strr:
	print("match found")
else:
	print("NO match found")
	
	
	
#Findall
#!
import re

strr=re.compile(r'\d\d\d\d\d\d\d\d\d\d')
res=strr.findall('i chane my mobile number from 1234567890 into  9000000049')

print(res)

if res:
	print("match found")
else:
	print("NO match found")


res='i own this number 9000000049 and 9874561230'
strr=re.findall(r'\d\d\d\d\d\d\d\d\d\d',res)

print(strr)	

if strr:
	print("match found")
else:
	print("NO match found")

	
	
#Split

import re

strr=re.compile(r'\d\d\d\d\d\d\d\d\d\d')
res=strr.split('i change my mobile number from 1234567890 into  9000000049')

print(res)

if res:
	print("match found")
else:
	print("NO match found")


res='i own this number 9000000049 and 9874561230'
strr=re.split(r'\d\d\d\d\d\d\d\d\d\d',res)

print(strr)	

if strr:
	print("match found")
else:
	print("NO match found")
  
 #split count 
import re

strr=re.compile(r'\d\d\d\d\d\d\d\d\d\d')
res=strr.split('i change my mobile number from 1234567890 into  9000000049',1)

print(res)

if res:
	print("match found")
else:
	print("NO match found")


res='i own this number 9000000049 and 9874561230'
strr=re.split(r'\d\d\d\d\d\d\d\d\d\d',res,1)

print(strr)	

if strr:
	print("match found")
else:
	print("NO match found")
  

  
 #sub 
#1
import re

strr=re.compile(r'\d\d\d\d\d\d\d\d\d\d')
res=strr.sub('mobile number','i change my mobile number from 1234567890 into  9000000049')

print(res)



res='i own this number 9000000049 and 9874561230'
strr=re.sub(r'\d\d\d\d\d\d\d\d\d\d','phone number',res)

print(strr)	



#re.subn
import re
res='i own this number 9000000049 and 9874561230'
strr=re.subn(r'\d\d\d\d\d\d\d\d\d\d','phone number',res)

print(strr)	

#.start() .end() .span()
import re

res='i own this number 9000000049'
strr=re.search(r'\d\d\d\d\d\d\d\d\d\d',res)

print(strr.start())
print(strr.end())
print(strr.span())

#group and groups
#1
import re 
var='This is my number 9162345-69871 and 7894561230'
def fun(no):
	stru=re.compile(r'((91)[6-9][0-9]{4})-([0-9]{5})')
	res=stru.search(no)
	print(res.groups())
	print(res.group())
fun(var)

#2

import re 
var='This is my number 9162345-69871 and 7894561230'
def fun(no):
	stru=re.compile(r'(91)([6-9])([0-9]{4})-([0-9]{5})')
	res=stru.search(no)
	print(res.groups())
	print(res.group())
fun(var)

#3
import re 
var='This is my number 9162345-69871 and 7894561230'
def fun(no):
	stru=re.compile(r'((91)[6-9][0-9]{2})([0-9]{2})-([0-9]{3})')
	res=stru.search(no)
	print(res.group())    #the last digit count will be grater than previous
fun(var)






#Meta-Characters
#1
#[],{}
import re

res='9000000049 into 9874561230'
strr=re.match(r'[0-9]',res)

print(strr)	

#2
import re

res='9000000049 into 9874561230'
strr=re.match(r'[0-9]{10}',res)

print(strr)	

#3
#\

import re

res='90'
strr=re.search('\d',res)

print(strr)	


res='90'
strr=re.match('\d',res)

print(strr)	

res='90'
strr=re.findall('\d',res)

print(strr)	

#4

#.


import re

res='98999522540'
strr=re.search('9.........0',res)

print(strr)	


# ^

#1
import re

res='98999522540 changed into 9092550000'
strr=re.findall('^98',res)

print(strr)	

#2
import re

res='98999522540 changed into 9092550000'
strr=re.findall('^90',res)

print(strr)	

# $
#1
import re

res='98999522540 changed into 9092550000'
strr=re.findall('00$',res)

print(strr)	
#2

import re

res='98999522540 changed into 9092550000'
strr=re.findall('40$',res)

print(strr)	


#'*' nad '+'
import re
#1
#1
res='i am good person and person with onemorepeaaaaa '
strr=re.findall('per*',res)
print(strr)

#2
res='i am good person and person with onemorepeaaaaa '
strr=re.findall('per*s',res)
print(strr)

#3
res='i am good person and person '
strr=re.search('per*s',res)
print(strr)

#4
res='i am good person'
strr=re.search('pex*',res)
print(strr)


#2
import re

#1
res='i am good person and person '
strr=re.findall('per+',res)
print(strr)

#2
res='i am good person and person '
strr=re.findall('per+s',res)
print(strr)

#3
res='i am good person and perrrrrson '
strr=re.findall('per+s',res)
print(strr)

#4
res='i am good person and person '
strr=re.search('pe+s',res)
print(strr)

#5
res='i am good person'
strr=re.search('pex+',res)
print(strr)

#'?'

import re
res='my moi mobile number is 9595959595'
strr=re.findall('mob?i',res)
print(strr)

res='my mobile number is 9595959595'
strr=re.findall('mob?l',res)
print(strr)

#'|''()'
import re
res='my mobile number is 9595959595'
strr=re.findall('(9)',res)
print(strr)

res='my mobile number is 9595959595'
strr=re.findall('(9|5)',res)
print(strr)

#Special Sequences
#1
"\A"
import re
res='my mobile number is 9595959595 my'
strr=re.findall('\Amy',res)
print(strr)

res='my mobile number is 9595959595'
strr=re.findall('\Anumber',res)
print(strr)

#2
#"\b\
import re
res='football , cricket, football'
strr=re.findall(r'\bfoo',res)
print(strr)

res='i am a football player hifoo'
strr=re.findall(r'foo\b',res)
print(strr)

#"\B\

import re
res='Thefootball , cricket, football'
strr=re.findall(r'\Bfoo',res)
print(strr)

res='i am a football player hifooHello'
strr=re.findall(r'foo\B',res)
print(strr)

#"\d\ and "\D"
import re
res='HI MY Number is 1234567890'
strr=re.findall(r'\d',res)
print(strr)

res='i am a football player '
strr=re.findall(r'\D',res)
print(strr)

#'\s\ and '\S'
import re
res='HI MY Number is 1234567890'
strr=re.findall(r'\s',res)
print(strr)

res='i am a football player '
strr=re.findall(r'\S',res)
print(strr)

#\w and \W

import re
res='HI MY_Number is 1234567890'
strr=re.findall(r'\w',res)
print(strr)

res='i @# am a %^ football player '
strr=re.findall(r'\W',res)
print(strr)

#\Z

import re
#1
res='HI MY_Number is 1234567890'
strr=re.findall(r'90\Z',res)
print(strr)

#2
res='i am a football player'
strr=re.findall(r'er\Z',res)
print(strr)

#3
res='HI MY_Number is 1234567890 '
strr=re.findall(r'er\Z',res)
print(strr)




#SET
#1
#[arn]
import re
res='my mobile number @# ^ is 9595959595 and we are friends '
strr=re.findall("[arn]",res)
print(strr)

#[^arn]

import re
res='my mobile number @# ^ is 9595959595 and we are friends '
strr=re.findall("[^arn]",res)
print(strr)


 #2
#[a-n]
import re
res='my mobile number @# ^ is 9595959595 and we are friends '
strr=re.findall("[a-n]",res)
print(strr)

#[^a-n]

import re
res='my mobile number @# ^ is 9595959595 and we are friends '
strr=re.findall("[^a-n]",res)
print(strr)


#3
#[012345],[1-5]
import re
res='my mobile number @# ^ is 9595959595 and we are friends '
strr=re.findall("[012345]",res)
print(strr)

import re
res='my mobile number @# ^ is 9595959595 and we are friends '
strr=re.findall("[0-5]",res)
print(strr)

#4
#[a-zA-Z],[a-zA-Z0-9_]
import re
res='my mobile number @# ^ is 9595959595 and we are friends '
strr=re.findall("[a-zA-Z]",res)
print(strr)

import re
res='_ my mobile number @# ^ is 9595959595 and we are friends '
strr=re.findall("[a-zA-Z0-9_]",res)
print(strr)


#special characters except "
#!@$%^&*()_+-={}|?><
import re
res='+my mobile number @# ^ is 9595959595 and we are friends '
strr=re.findall("[+]",res)
print(strr)

import re
res='_ my mobile number @# ^ is 9595959595  !&* and we are friends '
strr=re.findall("[+!@#$%^&*(A){}|:<>?]",res)
print(strr)









