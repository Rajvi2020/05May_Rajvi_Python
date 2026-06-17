# replace string 

import re
word="dog, bot , god , rose , not "
regex=re.compile("[b]ot")
word=regex.sub("Sample",word)
print(word)

'''b]ot

અહીં [] નો અર્થ character class થાય છે.

[b]

એનો અર્થ:

b

માત્ર b character.

એટલે:

[b]ot

અને

bot

બંને એકસરખું કામ કરે છે.

તો [] શા માટે વાપરાય?

કારણ કે character class માં એક કરતાં વધુ characters આપી શકાય.

Example:

[bgn]ot

અર્થ:

bot
got
not

ત્રણમાંથી કોઈપણ match થશે.'''

'''import re

word = "dog bot god"

x = re.sub("bot", "Sample", word)

print(x)

Output:

dog Sample god

આ perfectly ચાલે છે. ✅

Compile સાથે
import re

regex = re.compile("bot")

word = "dog bot god"

x = regex.sub("Sample", word)

print(x)

Output:

dog Sample god

આ પણ same output આપે છે. ✅

તો compile શા માટે?

ધારો એક જ pattern "bot" 10 જગ્યાએ વાપરવો છે.

Compile વગર:

re.findall("bot", txt1)
re.search("bot", txt2)
re.sub("bot", "Sample", txt3)
re.match("bot", txt4)

દર વખતે "bot" લખવું પડે.

Compile સાથે:

regex = re.compile("bot")

regex.findall(txt1)
regex.search(txt2)
regex.sub("Sample", txt3)
regex.match(txt4)

એક વાર pattern બનાવ્યો, પછી વારંવાર ઉપયોગ કર્યો.
સરળ ભાષામાં: compile() = regex pattern ને તૈયાર (pre-compile) કરીને object બનાવે જેથી એ જ pattern વારંવાર ઉપયોગ કરી શકાય.
'''