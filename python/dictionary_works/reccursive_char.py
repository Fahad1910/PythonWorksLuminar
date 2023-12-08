text="ABCDAB"

# first recursive character
wc={}

for ch in text:
    if ch in wc:
        print(ch ,"is the first recursive character ")
        break
    else:
        wc[ch]=1


# dictionary
# {}
# key:value
# fetch values by using key
# duplicate key is not allowed . values can be duplicate