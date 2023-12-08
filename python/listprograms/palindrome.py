
text="madam"

count=len(text)-1

palin_str=""

for i in range(count,-1,-1):
    palin_str+=text[i]
if(text==palin_str):
    print("Pallindrome")
else:
    print("not palindrome")




# print("palindrome" if text==palin_str else "not palindrome")