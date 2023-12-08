from re import *

variable=input("enter a variable name : ")

rule="[A-Za-z][\a-zA-Z0-9]*"        # * = zero or more 

matcher=fullmatch(rule,variable)
print("invalid" if matcher==None else "valid")


# rule
# k,,,m
# must be a digit and that / by 3
# any number of characters   