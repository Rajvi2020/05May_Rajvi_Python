class studinfo:
  stid=101
  stnm='rajvi'

  def getdata(self):
    print("id",self.stid)
    print("name",self.stnm)


    #Object
"""st=Studinfo()
#st.getdata()
st.stid=102
st.stnm="Nirav"
st.getdata()"""

#instance
studinfo().getdata()
studinfo().stid=102
studinfo().stnm='raj'
studinfo().getdata()

#it can't change varibales value
#can't modify
