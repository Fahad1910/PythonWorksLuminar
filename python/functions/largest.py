num1=int(input("enter the first number : "))
num2=int(input("enter the second number : "))
num3=int(input("enter the third number : "))

def largest(num1,num2,num3):
    if(num1>num2 and num1>num3):
        print(num1,"is largest")
    elif(num2>num1 and num2>num3):
        print(num2,"is largest")
    else:
        print(num3,"is largest")

largest(num1,num2,num3) 