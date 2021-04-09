from functions.functions import FactorInteger


sol = 0
i = 2
count = 0
while sol == 0:
    if len(FactorInteger(i)) == 4:
        count += 1
    else: 
        count = 0

    if count == 4:
        sol = i-3
    i += 1

print(sol)

