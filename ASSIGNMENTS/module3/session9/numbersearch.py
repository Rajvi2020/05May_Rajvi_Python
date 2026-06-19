import re
text = "For delivery contact Rahul at 9876543210 or customer care at 9123456789."
pattern = r"\b\d{10}\b"
match = re.search(pattern, text)
if match:
    print("Mobile Number:", match.group()) # to write no by printing directly match object will print.
else:
    print("No mobile number found")