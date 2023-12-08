# low_limit=int(input("enter lower limit : "))
# upp_limit=int(input("enter Upper limit : "))
# for i in range(low_limit,upp_limit):
#     print(i)


# low_limit=int(input("enter lower limit : "))
# upp_limit=int(input("enter Upper limit : "))
# for i in range(low_limit,upp_limit):
#     if(i%2==0):
#         print(i)


# print all numbers from l_limit to u_limit if num / by 3 print fizz if num / by 5 buzz
                            # if num / by 15 fizzbuzz
                            #else print number

low_limit=int(input("enter lower limit : "))
upp_limit=int(input("enter Upper limit : "))
for i in range(low_limit,upp_limit):
    if(i%3==0):
        print("fizz")
    elif(i%5==0):
        print("buzz")
    elif(i%15==0):
        print("fizzbuzz")
    else:
        print(i)