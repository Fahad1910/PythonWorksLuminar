from re import *

gmail=input("enter Gmail id : ")
rule="[a-z0-9][\W\w]+[@]gmail[.]com"

matcher=fullmatch(rule,gmail)
print("invalid" if matcher==None else "valid")



# password validate
# atleast 1 Uppercase
# atleast 1 special character
# minimum 8 character