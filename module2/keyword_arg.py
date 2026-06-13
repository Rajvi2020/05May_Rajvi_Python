def  myfunc(id,name,city="rajkot"):
   print("id:",id)
   print("name:",name)
   print("city:",city)
myfunc(id=101,city="surat",name="rajvi")


'''def myfunc(id,name,city="rajkot"):
Function માં 3 parameters છે: id, name, city.
city="rajkot" એ default argument છે.
જો city value ન આપો તો "rajkot" use થશે.


myfunc(id=101,city="surat",name="rajvi")
Values keyword arguments દ્વારા pass કરવામાં આવી છે.
Parameter નો order બદલાય તો પણ ચાલે.
અહીં city માટે "surat" આપ્યું હોવાથી default value "rajkot" use નહીં થાય.'''