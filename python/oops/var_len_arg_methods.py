def product(*args):
    res=1
    for n in args:
        res*=n
    print(res)

product(2,5)
product(2,5,6)



def greetings(**kwargs):
    print(f"hello {kwargs.get('msg')} app user {kwargs.get('user_name')}")

greetings(msg="good morning",user_name="Fahad")




# def dispatch_order(**kwargs):
#     print(f"hello user {kwargs.get('name')} your order {kwargs.get('code')} {kwargs.get('item')} is ready to {kwargs.get('status')}")

# # hello user vijay your order 123bc ucb shirt is ready to deliver
# dispatch_order(item="ucb shirt",code="123bc",status="deliver!",name="vijay")


def dispatch_order(**kwargs):
    item=kwargs.get("item")
    code=kwargs.get("code")
    status=kwargs.get("status")
    name=kwargs.get("name")
    print(f"hello user {name} your order {code} {item} is ready to {status}")


 # hello user vijay your order 123bc ucb shirt is ready to deliver
dispatch_order(item="ucb shirt",code="123bc",status="deliver!",name="vijay")