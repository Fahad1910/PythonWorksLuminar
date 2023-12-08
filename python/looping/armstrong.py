num=371
original=num
sum=0
while(num!=0):
    digit=num%10
    cube=digit**3
    sum+=cube
    num=num//10
print(sum)

print("armstrong"if sum==original else "not armstrong")