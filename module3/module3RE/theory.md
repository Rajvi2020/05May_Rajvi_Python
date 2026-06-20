એકદમ સરળ ભાષામાં 😄

### `r` (Raw String) શા માટે?

Python ને કહીએ છીએ:

> "ભાઈ, અંદર જે `\` છે એને જેમનું તેમ રાખજે, તું તેનો અર્થ કાઢતો નહીં."

---

### Example

```python
import re

re.findall(r'\d', "abc123")
```

અહીં:

```python
\d
```

નો અર્થ Regex માં **digit**.

Output:

```python
['1', '2', '3']
```

---

### `r` ન લખીએ તો?

```python
import re

re.findall('\d', "abc123")
```

આ case માં પણ output આવી જશે:

```python
['1', '2', '3']
```

એટલે તને લાગશે કે `r` ની જરૂર જ નથી. 😄

---

### પણ Problem ક્યાં આવે?

```python
re.findall('\bcat', "cat")
```

અહીં Python `\b` ને **backspace** સમજી શકે.

એટલે output ખોટું આવી શકે.

પણ:

```python
re.findall(r'\bcat', "cat")
```

અહીં Python `\b` ને બદલતું નથી.

Regex સુધી સાચું `\b` પહોંચે છે.

---

## સરળ નિયમ

### `r` સાથે

```python
r'\d'
```

Python કહે:

```text
લ્યો Regex, આ \d જેમનું તેમ
```

---

### `r` વગર

```python
'\d'
```

Python કહે:

```text
પહેલા હું check કરું કે \ નો કોઈ ખાસ અર્થ છે કે નહીં
```

---

## Exam માટે

```text
Raw String (r'') વાપરવાથી backslash (\) જેમનું તેમ રહે છે અને Regex patterns સાચી રીતે કામ કરે છે.
```

### સૌથી સરળ યાદ

```text
Regex લખો → r લગાવી દો
```

```python
r'\d'
r'\w'
r'\s'
r'\b'
```

આ safest અને recommended રીત છે. 👍


pyeuite similar to tkinter

