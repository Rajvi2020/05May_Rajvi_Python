def getdata(*data):
 print("id:",data[0])
 print("name:",data[1])
 print("city",data[2])
getdata(1,'sanket','rajkot')


#It allows a function to accept multiple values without fixing the number of arguments.
'''*args	**kwargs
Multiple positional arguments	Multiple keyword arguments
Tuple માં store થાય	Dictionary માં store થાય
* use થાય	** use થાય
Example Together
def myfunc(*args, **kwargs):
    print(args)
    print(kwargs)

myfunc(10, 20, name="Rajvi", city="Surat")

Output:

(10, 20)
{'name': 'Rajvi', 'city': 'Surat'}
One-Line Revision
*args → Multiple values → Tuple
**kwargs → Multiple keyword values → Dictionary ✅'''