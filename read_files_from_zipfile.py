from zipfile import *
import re
import csv
obj=ZipFile("/home/gopi/Videos/Zip.zip","r",ZIP_STORED)

obj=obj.namelist()
print(obj)
for i in obj:
	if re.search(".csv",i): 
		with open(i,"r") as d:
			for i in csv.reader(d):
				for j in i:
					print(j)
	elif re.search(".docx",i) :
		with open (i,"r") as e:
			print(e.read())
		
	
		