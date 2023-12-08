def decor1(f): # f num()
    def inner():
        x=f()   # 20
        return x*x  # 20*20=400
    return inner

def decor2(f):
    def inner():
        x=f()   # x=10
        return 2*x  #2*10=20
    return inner


@decor1
@decor2
def num():
    return 10

print(num())
