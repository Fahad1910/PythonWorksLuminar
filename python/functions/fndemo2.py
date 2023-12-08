def get_discount_price(actual_price,discount):
    sp=actual_price-(actual_price*discount)/100
    return sp
print(get_discount_price(50,10))