movie_budget = float(input())
statists = int(input())
dress_for_one_statist = float(input())

decor_sum = movie_budget * 0.10

if statists > 150:
    dress_for_one_statist *= 0.90

sum_for_all_statists = statists * dress_for_one_statist
movie_sum = decor_sum + sum_for_all_statists
total = movie_budget - movie_sum

if total >= 0:
    print("Action!")
    print(f"Wingard starts filming with {total:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {abs(total):.2f} leva more.")
