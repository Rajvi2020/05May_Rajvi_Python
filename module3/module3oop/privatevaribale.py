class studinfo:
  __stid=101
  __stnm="sanket"

  def __getdata(self):
    print("id",self.__stid)
    print("name:",self.__stnm)

  def fetchdata(self):
    self.__getdata()
st=studinfo()
st.fetchdata()