arr=[5,2,5,3,2]

arr.sort()

for i in range(0,len(arr)-1):
    current=arr[i]
    next=arr[i+1]

    if current==next:
        print(current)


# arr.sort()
# duplicate_list=[]

# for i in range(0,len(arr)-1):
#     current=arr[i]
#     next=arr[i+1]

#     if current==next:
#         if current not in duplicate_list:
#             duplicate_list.append(current)

# print(duplicate_list)
      

def decor1(f):
    def inner():
        x=f()
        return x*x
    return inner

def decor2(f):
    def inner():
        x=f()
        return 2*x
    return inner

def decor3(f):
    def inner():
        x=f()
        return 3*x
    return inner

class mobile:
    def __init__(self,*args,**kwargs):
        self.name=kwargs.get("name")

        
def value(x1,x2):
    value=x1+x2
    return value
print(2,3)
         
