import re   # Regular Expression module import kare chhe

mystr = "That is Python!1235659"   # String

# \w = word characters (A-Z, a-z, 0-9, _)
# x = re.findall('\w', mystr)

# \W = special characters and spaces
#x = re.findall('\W', mystr)

# \d = digits (0-9)
#x = re.findall('\d', mystr)

# \D = non-digits also includes special charaacters and spaces
#x = re.findall('\D', mystr)

# \s = whitespace (space, tab, newline)
#mystr = "Python_123 @GTU\tAhmedabad\n2026"
#x = re.findall('\s', mystr)

# \S = non-whitespace characters,એટલે કે space, tab (\t), newline (\n) સિવાયના બધા characters
#x = re.findall('\S', mystr)

# \b = word boundary par "This" search kare,Word Boundary એટલે શબ્દની શરૂઆત અથવા અંતની જગ્યા.
#x = re.findall(r'\bThis', mystr)

# \B = not a word boundary, "56" pela word boundary na hovi joie
#mystr = "That is Python!12356"
#mystr = "That is Python!123 56"  capital b will retur here [] but above return 56 because,
'''re.findall(r'\B56', mystr)
Case 1
mystr = "That is Python!12356"

અહીં:

12356
   ↑
  56

56 પહેલાં 3 છે.

3 = word character (\w)
5 = word character (\w)

બંને word characters છે.

એટલે ત્યાં word boundary નથી.

તેથી:

re.findall(r'\B56', mystr)

Output:

['56']
Case 2
mystr = "That is Python!123 56"

અહીં:

123 56
    ↑

56 પહેલાં space છે.

Space = non-word character
5 = word character

non-word પછી word શરૂ થાય એટલે word boundary (\b) બને.

એટલે ત્યાં \B match નહીં થાય.

re.findall(r'\B56', mystr)

Output:

[]'''
#x = re.findall('\B56', mystr)

# \A = string ni sharuat ma "This" hovu joie
#x = re.findall('\AThis', mystr)

# \Z = string na end ma "59" hovu joie
x = re.findall('59\Z', mystr)

print(x)   # Match male to list print kare