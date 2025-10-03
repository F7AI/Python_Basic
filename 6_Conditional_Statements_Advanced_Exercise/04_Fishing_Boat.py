group_budget = int(input())
season = input()
fisher_number = int(input())
shipt_rent_prie = 0

if season == 'Spring':
    shipt_rent_prie = 3000
elif season == 'Summer' or season == 'Autumn':
    shipt_rent_prie = 4200
elif season == 'Winter':
    shipt_rent_prie = 2600

if fisher_number <= 6:
    shipt_rent_prie *= 0.90
elif 7 <= fisher_number <= 11:
    shipt_rent_prie *= 0.85
else:
    shipt_rent_prie *= 0.75

if fisher_number % 2 == 0 and season != "Autumn":
    shipt_rent_prie *= 0.95

diff = group_budget - shipt_rent_prie

if diff >= 0:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(diff):.2f} leva.")
