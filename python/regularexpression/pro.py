from re import *

phone_rule="\d{10}"
mail_idrule="[a-z0-9][\W\w]+[@]gmail[.]com"

mail_ids=[]
phone_numbers=[]

path=open("C:\\Users\\Asus\\Desktop\\Luminar\\regularexpression\\data.txt","r")

for line in path:
    words=line.rstrip("\n").split(" ")
    for w in words:
        p_matcher=fullmatch(phone_rule,w)
        e_matcher=fullmatch(mail_idrule,w)
        if p_matcher!=None:
            phone_numbers.append(w)
        elif e_matcher!=None:
            mail_ids.append(w)

print(phone_numbers)
print(mail_ids)