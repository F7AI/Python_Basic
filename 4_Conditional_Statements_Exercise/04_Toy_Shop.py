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
# сметки:
order_price = ((number_puzzle * number_puzzle) + (number_dolls * number_dolls)
               + (number_bears * number_bears) + (number_minions * number_minions) + (number_trucks * number_trucks))
order_toys = number_puzzle + number_dolls + number_bears + number_minions + number_trucks
if order_toys >= 50:
    discount = order_price * 0.25
rent =