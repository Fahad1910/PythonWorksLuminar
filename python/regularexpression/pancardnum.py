# Rules
# first three characters must be upper case random alphabets
# 4th place must be alphabets(PCFHTA)
# 5th place any random uppercase
# 4 digits
# one alphabets

from re import *

pan_number=input("Enter pancard number : ")

rule="[A-Z]{3}[PCFHTA]{1}[A-Z]{1}[\d]{4}[A-Z]{1}"

matcher=fullmatch(rule,pan_number)

print("invalid" if matcher==None else "valid")