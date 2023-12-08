lst=[4,5,6,7,8,2,1]

# square=[]

# for i in lst:
#     square.append(i**2)


# new format: variable=[return - loop - condition]

square=[n**2 for n in lst]
# print(square)

cube=[n**3 for n in lst]
# print(cube)

evens=[n for n in lst if n%2==0]
# print(evens)

odd=[n for n in lst if n%2!=0]
# print(odd)

num_gtfive=[n for n in lst if n>=5]
print(num_gtfive)