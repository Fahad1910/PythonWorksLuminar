from re import *
text="goodmorning #sachin001"

# pattern="[aeiou]"

# consonants
pattern="[^aeiou\W\d]"
matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),m.group())
# print all vowels using re