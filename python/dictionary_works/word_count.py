text="hello hai hello hai"

#word count

word=text.split(" ") # words in text variable is splitted with space
wc={}

for w in word:
    if w in wc:
        wc[w]+=1
    else:
        wc[w]=1
print(wc)

# print(wc["hello"])