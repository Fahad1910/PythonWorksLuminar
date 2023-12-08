f=open("C:\\Users\\Asus\\Desktop\\Luminar\\file_operation\\numbers.txt")

all_numbers=[num.rstrip("\n") for num in f]
print(all_numbers)

kerala_num=[num for num in all_numbers if num.startswith("kl")]
print(kerala_num)