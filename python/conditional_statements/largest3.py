num1=int(input("enter num1 : "))
num2=int(input("enter num2 : "))
num3=int(input("enter num3 : "))

# Largest number

# if(num1>num2) and (num1>num3):
#     print("num1 is largest")
# elif(num2>num1) and (num2>num3):
#     print("num2 is largest")
# elif(num3>num2) and (num3>num1):
#     print("num3 is largest")
# elif(num1==num2) and (num1==num3):
#     print("all are equal")


# Second largest number

# if(num1>num2) and (num1>num3):
#     if(num2>num3):
#         print("num2 is second largest ")
#     else:
#         print("num3 is second  largest")

# elif(num2>num1) and (num2>num3):
#     if(num1>num3):
#         print("num1 is second largest")
#     else:
#         print("num3 is second largest")
# elif(num3>num2) and (num3>num1):
#     if(num2>num1):
#         print("num2 is second largest")
#     else:
#         print("num1 is second largest")
# elif(num1==num2) and (num1==num3):
#     print("all are equal")



# Sort number in descending order

if(num1>num2) and (num1>num3):
    if(num2>num3):
        print(num1,num2,num3)
    else:
        print(num1,num3,num2)

elif(num2>num1) and (num2>num3):
    if(num1>num3):
        print(num2,num1,num3)
    else:
        print(num2,num3,num1)
elif(num3>num2) and (num3>num1):
    if(num2>num1):
        print(num3,num2,num1)
    else:
        print(num3,num1,num2)
elif(num1==num2) and (num1==num3):
    print("all are equal")