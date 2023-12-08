# 1800-2024

years=[y for y in range(1800,2025)]
# print(years)

centuary_years=[y for y in years if y%100==0]
# print(centuary_years)

non_centuary_year=[y for y in years if y%100!=0]
print(non_centuary_year)