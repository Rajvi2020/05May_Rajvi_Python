def getvalue(a, b):
    return a, b


x = getvalue(12, 45)


def getsum():
    print("sum:", x[0] + x[1])


def getmul():
    print("mul:", x[0] * x[1])


getsum()
getmul()

"""Function એ બે values return કરે છે.
Multiple values return થાય ત્યારે Python તેને Tuple તરીકે store કરે છે.
Returned tuple ને variable માં store કરી શકાય છે.
Tuple ના elements ને index દ્વારા access કરી શકાય છે.
0 index પ્રથમ value દર્શાવે છે.
1 index બીજી value દર્શાવે છે.
Returned values નો ઉપયોગ કરીને અલગ-અલગ functions માં operations કરી શકાય છે.
આ program માં returned values પર addition અને multiplication operation કરવામાં આવ્યા છે.
Function નો ઉપયોગ code reusability અને modular programming માટે થાય છે."""
