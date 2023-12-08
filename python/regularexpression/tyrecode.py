# 3 digit
# /
# 2 digit R
# 2 digit
# /
# 2 digit 1 alphabets

from re import *

code=input("enter tyre code : ")

rule="[\d]{3}[/][\d]{2}[R][\d]{2}[/][\d]{2}[A-Z]"

matcher=fullmatch(rule,code)

print("invalid" if matcher==None else "valid")