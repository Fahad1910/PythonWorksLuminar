enquiries=["django","testing","django","bigdata","django","aws","aws","django"]

enquiry_count={}

for course in enquiries:
    if course in enquiry_count:
        enquiry_count[course]+=1
    else:
        enquiry_count[course]=1

print(enquiry_count)