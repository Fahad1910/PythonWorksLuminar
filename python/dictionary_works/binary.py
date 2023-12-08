# Binary search
# worst case
# edge case

lst=[12,3,4,15,16,18]

lst.sort()
print(lst)
element=18
low=0
upp=len(lst)-1
is_found=False

while(low<=upp):
    mid=(low+upp)//2

    if element==lst[mid]:
        is_found=True
        break
    elif element<lst[mid]:
        upp=mid-1
    elif element>lst[mid]:
        low=mid+1

print(is_found)