class master:
  def signin(self,unm,pas):
    if unm=='admin' and pas=="admin":
      print("login success")
    else:
      print("error")

class home(master):
  def signin(self,unm,pas):
    return super().signin(unm,pas)

class about(master):
  def signin(self,unm,pas):
    return super().signin(unm,pas) 

m=master()
m.signin('admin','admin')
h=home()
h.signin('a',1)
a=about()
a.signin('admin','admin')

       
      