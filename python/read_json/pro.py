from json import load
path="C:\\Users\\Asus\\Desktop\\Luminar\\read_json\\data.json"
with open(path)as f:
    records=load(f)

# print(len(records))

# for f in records:
#     print(f.get("name"))

fw_names=[f.get("name") for f in records]
# print(fw_names)

top_fw=max(records,key=lambda d: d.get("rating"))
# print(top_fw)


# print python frame works
# for r in records:
#     if r.get("language")=="python":
#         print(r.get("name"))

pyth_fw=[r.get("name") for r in records if r.get("language")=="python"]
print(pyth_fw)
 

# print backend framework
# for r in records:
#     if(r.get("side")=="backend"):
#         print(r.get("name"))

backend_fw=[r.get("name") for r in records if r.get("side")=="backend"]
print(backend_fw)
 

