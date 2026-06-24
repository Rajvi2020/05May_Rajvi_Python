# import random
# #x=random.random()
# #x=random.randint(111,99999)
# #x=random.randrange(1111,9999,120)
# captcha=random.choice['dfw','fwefr','fwfr']
# x=random.choice(captcha)
# print(x)

import random

captcha = ['dfw', 'fwefr', 'fwfr']
random.shuffle(captcha)
#x = random.choice(captcha)
print(captcha)
#print(x)

'''random.random()
0.0 (include) થી 1.0 (exclude) વચ્ચે random decimal number આપે છે.

random.randint(a,b)
a અને b બંને include થાય છે.
Example: random.randint(1,10) → 1 થી 10 વચ્ચે કોઈપણ number (1 અને 10 પણ આવી શકે).

random.randrange(start,stop)
start include થાય છે, stop include થતું નથી.
Example: random.randrange(1,10) → 1 થી 9 વચ્ચે number આપે.



random.randrange(start,stop,step)
start include, stop exclude.
Example: random.randrange(10,50,5) → 10, 15, 20, 25, 30, 35, 40, 45 માંથી random number આપે.
random.choice(sequence)
આપેલી list, tuple અથવા string માંથી એક random element પસંદ કરે છે.
Example: random.choice(['A','B','C']) → A, B અથવા C.
random.shuffle(list)
List ના બધા elements નો order randomly બદલે છે.
Original list modify થાય છે.
Example: [1,2,3,4] → [3,1,4,2]'''