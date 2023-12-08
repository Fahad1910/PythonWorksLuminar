all_users=["sachin","rahul","rohit","kohli","dravid","laxman","ganguly"]
sachin_following=["rahul","ganguly","dravid"]


sachin_sug=set(all_users).difference(set(sachin_following))
sachin_sug.remove("sachin")
print(sachin_sug)