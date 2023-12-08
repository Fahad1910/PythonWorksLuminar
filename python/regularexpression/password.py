# password validate
# atleast 1 Uppercase
# atleast 1 special character
# atleast 1 digit
# minimum 8 character

from re import *

password="Password@123"

# +ve look ahead assertion
rule="(?=.*[A-Z])(?=.*[\W](?=.*[\d])).{8,}"                      #  "?=."  => cursor position does not have priority 

matcher=fullmatch(rule,password)

print("invalid" if matcher==None else "valid")