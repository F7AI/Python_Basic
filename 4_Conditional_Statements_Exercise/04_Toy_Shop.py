# Вход
excursion_price = float(input())
puzzles = int(input())
talking_dolls = int(input())
teddy_bears = int(input())
minions = int(input())
trucks = int(input())

# Цени на играчките
puzzle_price = 2.60
talking_doll_price = 3.00
teddy_bear_price = 4.10
minion_price = 8.20
truck_price = 2.00

# Изчисляване на общата сума
total_price = (
    puzzles * puzzle_price +
    talking_dolls * talking_doll_price +
    teddy_bears * teddy_bear_price +
    minions * minion_price +
    trucks * truck_price
)

# Общо брой на играчките
total_toys = puzzles + talking_dolls + teddy_bears + minions + trucks

# Проверка за отстъпка
if total_toys >= 50:
    total_price *= 0.75  # 25% отстъпка

# Наем 10%
rent = total_price * 0.10
profit = total_price - rent

# Проверка дали парите стигат
if profit >= excursion_price:
    money_left = profit - excursion_price
    print(f"Yes! {money_left:.2f} lv left.")
else:
    money_needed = excursion_price - profit
    print(f"Not enough money! {money_needed:.2f} lv needed.")