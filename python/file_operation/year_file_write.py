yw=open("C:\\Users\\Asus\\Desktop\\Luminar\\file_operation\\year.txt","w")
# 1800-2024

for y in range(1800,2025):
    yw.write(str(y)+"\n")

yw.close()

# read from years.txt
fr=open("C:\\Users\\Asus\\Desktop\\Luminar\\file_operation\\year.txt","r")

years=[f.rstrip("\n") for f in fr]
print(years)

fr.close()





