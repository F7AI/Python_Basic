# •	Брой пилешки менюта – цяло число в интервала [0 … 99]
# •	Брой менюта с риба – цяло число в интервала [0 … 99]
# •	Брой вегетариански менюта – цяло число в интервала [0 … 99]
number_chiken_menu = int(input())
number_fish_menu = int(input())
number_vegatable_menu = int(input())
# Цени
chiken_menu = 10.35
fish_menu = 12.40
vegatable_menu = 8.15
delivery = 2.50
# оща цена на поръчката:
menu_cost = (number_chiken_menu * chiken_menu) + (number_fish_menu * fish_menu) \
                + (number_vegatable_menu * vegatable_menu)
desert_cost = menu_cost * 20 / 100
all_food_cost = menu_cost + desert_cost + delivery
print(all_food_cost)
