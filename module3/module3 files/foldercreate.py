import os
#print(file.read()) first this 
os.chdir("newfolder")
file=open("hii.txt",'w')
file.write("by")
file.close()
file1=open("hii.txt",'r')
print(file1.read())