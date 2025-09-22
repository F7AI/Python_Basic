# •	Пакет химикали - 5.80 лв.
# •	Пакет маркери - 7.20 лв.
# •	Препарат - 1.20 лв (за литър)
number_of_pens = int(input())
number_of_markers = int(input())
liters_of_chemicls = int(input())
procente_of_discount = int(input())

pens_price = 5.80
merkes_price = 7.20
chemicals_price = 1.20

total_pr = (number_of_pens * pens_price) + (number_of_markers * merkes_price) + (liters_of_chemicls * chemicals_price)
discount = total_pr * (procente_of_discount / 100)
final_price = total_pr - discount
print(final_price)
