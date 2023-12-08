# text="coffee"

# # for ch in text:
# #     if(ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u"):
# #         print(f"{ch} is vowel")
   

# for ch in text:
#     if ch in["a","e","i","o","u"]:
#         print(ch)
# in membership operartor


text="eatyaiicofee"
v_count=0
c_count=0

for ch in text:
    if ch in["a","e","i","o","u"]:
        v_count+=1
    else:
        c_count+=1
    
print("vowel count",v_count)
print("consanant count",c_count)