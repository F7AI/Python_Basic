Petar_budget = float(input())
gpu_amount = int(input())
cpu_amount = int(input())
ram_amount = int(input())

gpu_price = 250

money_gpu = gpu_amount * gpu_price
money_cpu = money_gpu * 0.35 * cpu_amount
money_ram = money_gpu * 0.10 * ram_amount

total_price = money_ram + money_cpu + money_gpu
if gpu_amount > cpu_amount:
    total_price *= 0.85
money_left = Petar_budget - total_price
if Petar_budget >= total_price:
    print(f"You have {money_left:.2f} leva left!")
else:
    print(f"Not enough money! You need {abs(money_left):.2f} leva more!")
