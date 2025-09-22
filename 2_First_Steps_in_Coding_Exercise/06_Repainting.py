amount_nylon = int(input())
amount_paint = int(input())
amount_thiner = int(input())
hours_for_compleate = int(input())
# цени на стоките!
nylon = 1.50
paint = 14.50
thiner = 5.00
bag_price = 0.40

nylon_total = amount_nylon + 2
paint_toral = amount_paint + (amount_paint * 0.10)

total_price = (nylon_total * nylon) + (paint_toral * paint) + (amount_thiner * thiner) + bag_price
workers_price = total_price * 30/100 * hours_for_compleate
print(total_price + workers_price)