city = input()
sales = float(input())
procentage = 0
if sales < 0 or city not in ['Sofia', 'Varna', 'Plovdiv']:
    print("error")
    exit()
if city == 'Sofia':
    if 0 <= sales <= 500:
       procentage = 0.05 * sales
    elif 500 <= sales <= 1000:
       procentage = 0.07 * sales
    elif 1000 <= sales <= 10000:
       procentage = 0.08 * sales
    elif sales >= 10000:
       procentage = 0.12 * sales
elif city == 'Varna':
    if 0 <= sales <= 500:
       procentage = 0.045 * sales
    elif 500 <= sales <= 1000:
       procentage = 0.075 * sales
    elif 1000 <= sales <= 10000:
       procentage = 0.10 * sales
    elif sales >= 10000:
       procentage = 0.13 * sales
elif city == 'Plovdiv':
    if 0 <= sales <= 500:
       procentage = 0.055 * sales
    elif 500 <= sales <= 1000:
       procentage = 0.080 * sales
    elif 1000 <= sales <= 10000:
       procentage = 0.12 * sales
    elif sales >= 10000:
       procentage = 0.145 * sales

print(f"{procentage:.2f}")

