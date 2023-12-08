from json import load
path="C:\\Users\\Asus\\Desktop\\Luminar\\countries\\countries.json"
with open(path,encoding="utf-8") as f:
    countries=load(f)

# print(len(countries))

country_name=[c.get("name") for c in countries]
# print(country_name)

# capital of china
country_capital=[c.get("capital") for c in countries if c.get("name")=="China"]
# print(country_capital)

# print region
region_name=[c.get("region") for c in countries]
# print(set(region_name))

country_borders=[c.get("borders") for c in countries if c.get("name")=="India"][0]
# print(country_borders)

border_name=[c.get("name") for c in countries if c.get("alpha3Code") in country_borders]
# print(border_name)

# print independent country names
independent_country=[c.get("name") for c in countries if c.get("independent")==True]
# print(independent_country)

# print currency name of india
country_details=[c.get("currencies") for c in countries if c.get("name")=="India"][0][0]
# print(country_details.get("name"))

# print country not using currency
data=[c.get("name") for c in countries if "currencies" not in c]
# print(data)

# # print countries with currency
# country_currencies=[c for c in countries if "currencies" in c]
# currencies=[cur.get("name") for c in country_currencies for cur in c.get("currencies")]
# # print(currencies)

country_currencies=[c for c in countries if "currencies" in c]
currencies=[cur.get("symbol") for c in country_currencies for cur in c.get("currencies")]
wc={}
for c in currencies:
    if c in wc:
        wc[c]+=1
    else:
        wc[c]=1

print(max((v,k) for k,v in wc.items()))