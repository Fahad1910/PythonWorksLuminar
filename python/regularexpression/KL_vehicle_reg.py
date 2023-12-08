# starts with KL
# 2 digit
# alphabet min 1 max 2
# digit 4

from re import *

vehicle_num=input("enter vehicle number : ")

rule="(KL)-[\d]{2}-[A-Z]{1,2}-[\d]{4}"

matcher=fullmatch(rule,vehicle_num)

print("invalid" if matcher==None else "valid")