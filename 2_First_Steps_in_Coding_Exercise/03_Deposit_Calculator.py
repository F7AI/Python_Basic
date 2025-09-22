# 1.	Депозирана сума – реално число в интервала [100.00 … 10000.00]
# 2.	Срок на депозита (в месеци) – цяло число в интервала [1…12]
# 3.	Годишен лихвен процент – реално число в интервала [0.00 …100.00]
deposit = float(input())
term_of_deposit = int(input())
Annual_interest_rate = float(input())

montly_interest = (deposit * Annual_interest_rate) / 100 / 12
final_amount = deposit + term_of_deposit * montly_interest
print(final_amount)