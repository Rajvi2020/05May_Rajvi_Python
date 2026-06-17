import re

text = "123-45-6789"

pattern = re.compile(r"""
\d{3}      # First 3 digits
-          # Hyphen
\d{2}      # Next 2 digits
-          # Hyphen
\d{4}      # Last 4 digits
""", re.VERBOSE) #or re.X pan lakhi sakiye

x = pattern.findall(text)

print(x)


'''
અહીં `re.X` (Verbose Mode) નું સંપૂર્ણ example:

```python
import re

text = "123-45-6789"

pattern = re.compile(r"""
\d{3}      # First 3 digits
-          # Hyphen
\d{2}      # Next 2 digits
-          # Hyphen
\d{4}      # Last 4 digits
""", re.X)

x = pattern.findall(text)

print(x)
```

### Output

```python
['123-45-6789']
```

---

### `re.X` વગર એ જ code

```python
import re

text = "123-45-6789"

pattern = re.compile(r"\d{3}-\d{2}-\d{4}")

x = pattern.findall(text)

print(x)
```

### Output

```python
['123-45-6789']
```

---

### Viva માં શું બોલવું?

* `re.X` = `re.VERBOSE`
* Regex માં **spaces અને comments** લખવાની છૂટ આપે છે.
* Long regex patterns ને વાંચવામાં સરળ બનાવે છે.
* Matching result બદલાતું નથી.


> `re.X (VERBOSE) modifier is used to make regular expressions more readable by allowing whitespace and comments inside the pattern.` ✅


'''