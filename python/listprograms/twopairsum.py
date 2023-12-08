lst=[2,3,4,5]
sum=8
count=1

low=0
upp=len(lst)-1
while(low<upp):
    cur_sum=lst[low]+lst[upp]
    if cur_sum==sum:
        print("pairs",lst[upp],lst[low])
        break
    elif cur_sum<sum:
        low+=1
    else:
        upp-=1
    count+=1

print(count)





# for i in range(0,len(lst)):
#     for j in range(i+1,len(lst)):
#         cur_sum=lst[i]+lst[j]
#         if cur_sum==sum:
#             print(lst[i],lst[j])
#             break