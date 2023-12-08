from re import  *

# text="ababbnababa"

# pattern="ab"
# matcher=finditer(pattern,text)

# for m in matcher:
#     print(m.start(),m.group())



# text="Python @ 123"
# # pattern="[a-z]" # check for all lowercase alphabets
# # pattern="[A-Z]" # check for all Uppercase alphabets
# # pattern="[a-zA-Z]" # all alphabets
# # pattern="[0-9]" # all digits
# pattern="[a-zA-Z0-9]" # alpha numeric

# pattern="[^]" # exclude
    # eg: pattern="[^a-zA-Z]" in this pattern excludes the alphabetic character lower and upper
# pattern="\d" #[0-9] # also used for digits
# pattern="\D" #"[^0-9]" excludes digit
# pattern="\w" # alphabets and numbers "[a-zA-Z0-9]"
# pattern="\W" # special character

# matcher=finditer(pattern,text)


# for m in matcher:
#     print(m.start(),m.group())



text="ababa123ABC@_"

# pattern="[^a-zA-Z0-9]"

# pattern="\d" #"[0-9]

# pattern="\D" #"[^0-9]"

# pattern="\w" # alphabets and numbers "[a-zA-Z0-9]"

pattern="\W" # special character

matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),m.group())

