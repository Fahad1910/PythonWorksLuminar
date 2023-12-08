orders=["vegmeals","fishmeals","vegmeals"
        ,"fishmeals","vb","cb","bb","vb","cb","bb",
        "bb","vb","fried_rice"]


order_count={}

for item in orders:
    if item in order_count:
        order_count[item]+=1

    else:
        order_count[item]=1

print(order_count)