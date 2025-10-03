month = input()
number_of_nights = int(input())

apartment = 0
studio = 0

if month == "May" or month == "October":
    studio = 50 * number_of_nights
    apartment = 65 * number_of_nights
    if number_of_nights > 14:
        studio *= 0.70   # 30% по-евтино
        apartment *= 0.90
    elif number_of_nights > 7:
        studio *= 0.95   # 5% по-евтино

elif month == "June" or month == "September":
    studio = 75.20 * number_of_nights
    apartment = 68.70 * number_of_nights
    if number_of_nights > 14:
        studio *= 0.80   # 20% по-евтино
        apartment *= 0.90

elif month == "July" or month == "August":
    studio = 76 * number_of_nights
    apartment = 77 * number_of_nights
    if number_of_nights > 14:
        apartment *= 0.90   # само апартаментът има намаление

print(f"Apartment: {apartment:.2f} lv.")
print(f"Studio: {studio:.2f} lv.")
