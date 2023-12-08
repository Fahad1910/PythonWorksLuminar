# BMI
# body mass index
# bmi=(weight in kg)/height in meter square

weight_kg=72
heightin_cm=165

# cm=>meter cm/100

heightin_m=(heightin_cm/100)

bmi=(weight_kg)/heightin_m**2
print("BMI =",bmi)