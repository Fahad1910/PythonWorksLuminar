# expenses=[12000,13000,14000,11000,25000,28000,21000]

# #print march month expense

# print("march expense : ",expenses[2])

# #print all expense

# for e in expenses:
#     print(e)


# #print costly expense

# max_exp=0
# for e in expenses:
#     if e>max_exp:
#         max_exp=e
# print(max_exp)


# #print expense > than 16000

# for e in expenses:
#     if(e>16000):
#         print(e)

# cheapest exp

# min_exp=expenses[0]

# for e in expenses:
#     if e<min_exp:
#         min_exp=e
# print(min_exp)



expenses=[12000,13000,14000,11000,25000,28000,21000]

# sorted(),Sum(),min(),max()

srt_exp=sorted(expenses,reverse=False) #ascending
print(srt_exp)

desc_srt=sorted(expenses,reverse=True) #descending
print(desc_srt)

total_exp=sum(expenses) # sum
print(total_exp)

max_exp=max(expenses)
print(max_exp)

min_exp=min(expenses)
print(min_exp)



