from re import *

text="aabbaaac"
#     01234567

# pattern="a+" #+ one or more a
# pattern="a*" # zero or more a
pattern="a{1,2}" # min 1 a or max 2 a

matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),m.group())

