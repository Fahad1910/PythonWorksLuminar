# ternary operator

num=int(input("enter the number : "))


# result="+ve" if num>0 else "-ve" #
# print(result)


result="+ve" if num>0 else "-ve" if num<0 else "zero"  # when there is more than 1 condition applied
print(result)