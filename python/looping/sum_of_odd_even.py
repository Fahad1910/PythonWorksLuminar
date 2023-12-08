# sum of all odd numbers range given by user
# sum of all even numbers range given by user

# start=int(input("enter the range : "))
# end=int(input("enter the range : "))
# sum=0
# while(start<=end):
#     if(start%2!=0):
#         sum+=start
#     start+=1
# print("sum of all odd : ",sum)


start=int(input("enter the range : "))
end=int(input("enter the range : "))
sum=0
while(start<=end):
    if(start%2==0):
        sum+=start
    start+=1
print("sum of all even : ",sum)