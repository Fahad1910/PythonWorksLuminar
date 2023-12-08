height_cm=int(input("enter your height : "))
weight_kg=int(input("enter your weight : "))

height_meter=height_cm/100
print(height_meter)

bmi=weight_kg//height_meter**2
print("bmi is =",bmi)

# <19 lightweight
# 20-25 normal
# 25-30 pre obesity
# >30 is obesity