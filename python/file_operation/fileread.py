f=open("C:\\Users\\Asus\\Desktop\\Luminar\\file_operation\\data.txt","r")

# for line in f:
#     print(line)


# words=[]
# for line in f:
#     words.append(line.rstrip("\n"))                 # strip used to remove => rstrip used to remove from right,
# print(words)                                        # lstrip used to remove from left



words=[line.rstrip("\n") for line in f]
print(words)