excursion = int(input())
number_puzzle = int(input())
number_dolls = int(input())
number_bears = int(input())
number_minions = int(input())
number_trucks = int(input())
# цени:
price_puzzle = 2.60
price_doll = 3
price_bear = 4.10
price_minion = 8.20
price_truck = 2

all_toys_price = ((number_puzzle * price_puzzle) + (number_dolls * price_doll)
            + (number_bears * price_bear) + (price_truck * price_truck))
number_toys = number_puzzle + number_dolls + number_bears + number_minions + number_trucks
if number_toys >= 50:
    all_toys_price = all_toys_price * 0.75

print(all_toys_price)
