days = int(input())
room_type = input()
rating = input()

nights = days - 1  # защото броят нощувки = дни - 1

price_per_night = 0

# Цени по тип помещение
if room_type == "room for one person":
    price_per_night = 18.00
elif room_type == "apartment":
    price_per_night = 25.00
elif room_type == "president apartment":
    price_per_night = 35.00

# Начална цена за целия престой
total_price = nights * price_per_night

# Намаления според типа помещение и броя нощувки
if room_type == "apartment":
    if days < 10:
        total_price *= 0.70
    elif 10 <= days <= 15:
        total_price *= 0.65
    else:
        total_price *= 0.50

elif room_type == "president apartment":
    if days < 10:
        total_price *= 0.90
    elif 10 <= days <= 15:
        total_price *= 0.85
    else:
        total_price *= 0.80
# "room for one person" няма отстъпка

# Оценка на престоя
if rating == "positive":
    total_price *= 1.25
elif rating == "negative":
    total_price *= 0.90

# Финален резултат
print(f"{total_price:.2f}")
