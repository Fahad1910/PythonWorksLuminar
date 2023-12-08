# print all odd numbers with in a given range(end)

# start=1
# range=int(input("enter the terminating range : "))
# # while(start<=range):
# #     print(start)
# #     start=start+2

# while(start<=range):
#     if(start%2!=0):
#         print(start)
#     start=start+1


# print all numbers which are divisible by 3 and 5 upto given range (start , end -user)

i=int(input("enter the start number : "))
i1=int(input("enter the end number : "))

while(i<=i1):
    if(i%3==0 and i%5==0):
        print(i)
    i+=1

