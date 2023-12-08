# for row in range(1,4):
#     for column in range(1,4):
#         print(row,end="\t")
#     print()



# for row in range(1,4):
#     for column in range(row):
#         print("#",end="\t")
#     print()


# for row in range(1,6):
#     for column in range(row):
#         print(row,end="\t")
#     print()


# for row in range(1,4):
#     for column in range(row):
#         print(column+1,end="\t")
#     print()


# for row in range(1,6):
#     for column in range(row):
#         res=column+1
#         if res%2==0:
#             print("#",end="\t")
#         else:
#             print(res,end="\t")
#         # print(column+1,end="\t")
#     print()


for row in range(4,0,-1):
    for column in range(row):
        print("#",end="\t")
    print()


