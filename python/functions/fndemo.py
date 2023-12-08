# def add(n1,n2):
#     res=n1+n2
#     return res

# print(add(40,50))


# def cube(n):
#     res=n**3
#     return res

# print(cube(3))


# def max_two(n1,n2):
#     if(n1>n2):
#         return n1
#     else:
#         return n2
    
# print(max_two(6,8))
    
    
# def max_two(n1,n2):
#     return n1 if n1>n2 else n2

# print(max_two(50,100))


# def sub(n1,n2):
#     return n1-n2
# print(sub(10,5))
# print(sub(5,10))


# def smart_sub(n1,n2):
#     if n1>n2:
#         return n1-n2           # return n1-n2 if n1>n2 else n2-n1
#     else:
#         return n2-n1
# print(smart_sub(5,10))
# print(smart_sub(10,5))



# def odd_even(num):
#     return "even" if num%2==0 else "odd"
# print(odd_even(3))


def hcf(num1,num2):
    res=1
    sm_num=num1 if num1<num2 else num2
    for i in range(1,sm_num+1):
        if num1%i==0 and num2%i==0:
            res=i
    return res

num1=int(input("enter the num1 : "))
num2=int(input("enter the num2 : "))
print(hcf(num1,num2))


# lcm

# lcm(num1,num2)=num1*num2/hcf(num1,num2)


def lcm(num1,num2):
    gcd=hcf(num1,num2)
    res=(num1*num2)/gcd

    return res
print(lcm(18,24))


def least_common_multiple(n1,n2):
    max=n1 if n1>n2 else n2
    flag=True

    while(flag):
        if max%n1==0 and max%n2==0:
            print(f"lcm of {n1},{n2} is {max}")
            break
        else:
            max+=1

least_common_multiple(30,25)