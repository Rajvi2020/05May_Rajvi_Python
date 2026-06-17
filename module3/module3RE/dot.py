import re
mystr='this is python'
'''# x = re.findall('py..on', mystr)

અહીં . નો અર્થ કોઈપણ એક character.

py..on

એટલે:

py + 2 characters + on'''
#x=re.findall('py..on',mystr)

'''import re

mystr = 'this is python'

x = re.findall('this|that', mystr)

print(x)
Meaning
'this|that'

નો અર્થ:

this OR that

Regex માં | = OR operator

તમારા string માં
mystr = "this is python"

Regex શોધે છે:

this મળે છે? ✅
that મળે છે? ❌

એટલે Output:

['this']
Example 2
mystr = "that is python"

x = re.findall('this|that', mystr)

print(x)

Output:

['that']
Example 3
mystr = "this and that"

x = re.findall('this|that', mystr)

print(x)

Output:

['this', 'that']

કારણ કે બંને words હાજર છે.'''
x=re.findall('this|that',mystr)
print(x)
'''in Regular Expression, dot (.) is a metacharacter that matches any single character except a newline character. For example, the pattern py..on can match python, py12on, or pyABon because the two dots represent any two characters."'''
