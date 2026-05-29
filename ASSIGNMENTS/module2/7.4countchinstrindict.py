str1="python programming"
count={}
for ch in str1:
    if ch in count:
        count[ch]+=1
    else:
        count[ch]=1
print(count)