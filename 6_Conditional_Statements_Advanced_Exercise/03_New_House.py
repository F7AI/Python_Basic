flower_type = input()
number_flowers = int(input())
budget = int(input())

roses_price = 5
dalia_price = 3.80
lale_price = 2.80
narcis_price = 3
gladiola_price = 2.50

total_price = 0

if flower_type == "Roses":
    total_price = number_flowers * roses_price
    if number_flowers > 80:
        total_price *= 0.90   

elif flower_type == "Dahlias":
    total_price = number_flowers * dalia_price
    if number_flowers > 90:
        total_price *= 0.85

elif flower_type == "Tulips":
    total_price = number_flowers * lale_price
    if number_flowers > 80:
        total_price *= 0.85

elif flower_type == "Narcissus":
    total_price = number_flowers * narcis_price
    if number_flowers < 120:
        total_price *= 1.15

elif flower_type == "Gladiolus":
    total_price = number_flowers * gladiola_price
    if number_flowers < 80:
        total_price *= 1.20

if budget >= total_price:
    print(f"Hey, you have a great garden with {number_flowers} {flower_type} and {budget - total_price:.2f} leva left.")
else:
    print(f"Not enough money, you need {total_price - budget:.2f} leva more.")
