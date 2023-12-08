

# def swap_num(fn):
#     def wrapper(n1,n2):
#         if n1<n2:
#             (n1,n2)=(n2,n1)
#         return fn(n1,n2)
#     return wrapper

# def smart_div(fn):
#     def wrapper(n1,n2):
#         # print("n1 is smart div",n1)
#         # print("n2 is smart div",n2)
#         if n2==0:
#             print("/ by zero nop")
#             return
#         return fn(n1,n2)
#     return wrapper
    

# @swap_num
# def sub(n1,n2):
#     return n1-n2

# @swap_num
# @smart_div
# def div(n1,n2):
#     return n1/n2

# print(sub(5,10))
# print(div(5,0))



def decorator1(fn):
    def wrapper():
        print("decorator 1 before calling original function")
        result=fn()
        print("decorator 1 after calling original function")
        return result
    return wrapper

def decorator2(fn):
    def wrapper():
        print("decorator 2 before calling original function")
        result=fn()
        print("decorator 2 after calling  original function")
        return result
    return wrapper


@decorator1
@decorator2
def original_function():
    print("this is original function")


original_function()
             