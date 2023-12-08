person={"name":"Fahad","age":21,"gender":"male"}
# print(person["name"])
# print(person["gender"])


# if salary is present add bonus of 2000rs else set salary as 30000

if "salary" in person:
    person["salary"]+=2000

else:
    person["salary"]=30000

print(person)