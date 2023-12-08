source_word="chicken"
target_word="hen"

source_wrd_lst=[]
kangaroo_string=""

for ch in source_word:
    source_wrd_lst.append(ch)

for ch in target_word:
    if ch in source_wrd_lst:
        source_wrd_lst.pop(source_wrd_lst.index(ch))
        kangaroo_string+=ch


print("kangaroo" if kangaroo_string==target_word else "not Kangaroo")


# print(kangaroo_string==target_word)