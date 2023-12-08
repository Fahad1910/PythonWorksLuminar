text="hello hai goodafternoon"

# longest word

words=text.split(" ")
longest_word=max(words,key=lambda w:len(w))

print(longest_word)

# smallest word
s_word=min(words,key=lambda w:len(w))
print(s_word)

# sorted in descending order
srt=sorted(words,reverse=True,key=lambda w:len(w))
print(srt)