# print a year is leap year or not 
# year = 


year=int(input("enter the year : "))

# if(year%4==0):           #(year%100!=0) or (year%400==0):
#     print("this is leap year")
# else:
#     print("it is not leap year")


if(year%100==0) and (year%400==0):
    print("leap year")
elif(year%100!=0) and (year%4==0):
    print("leap year")
else:
    print("not leap year")