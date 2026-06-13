class tops:
  stid=101
  stname="rajvi"
  def getdata(self):
    print("this is class")
  def getsum(self,a,b):
    print("sum:",a+b)

tp=tops()
print("id:",tp.stid)
print(tp.stname)
tp.getdata()
tp.getsum(23,45)

