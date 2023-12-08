# print words starting with vowels 

text="python is a programming language"

vowels=("a","e","i","o","u")

words=text.split(" ")

for w in words:
    if w.casefold().startswith(vowels):
        print(w)