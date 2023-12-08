# read from years.txt
# write leapyears in to leap.txt
# write nonleapyear into nonleap.txt

f_read=open("C:\\Users\\Asus\\Desktop\\Luminar\\file_operation\\year.txt","r")
l_write=open("C:\\Users\\Asus\\Desktop\\Luminar\\file_operation\\leapyear.txt","w")


for year in f_read:
    year=int(year)

    if (year%100==0) and (year%400==0):
        l_write.write(str(year)+"\n")
    elif(year%100!=0) and (year%4==0):
        l_write.write(str(year)+"\n")

# [l_write.write(str(year)+"\n") for year in f_read if int(year)%4==0] 