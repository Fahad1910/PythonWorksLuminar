# rule
# k,,,m
# must be a digit and that / by 3
# any number of characters   

from re import *

variable=input("enter a variable name : ")

rule="[k-m][369]\w*"

matcher=fullmatch(rule,variable)
print("invalid" if matcher==None else "valid")