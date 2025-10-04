stay_days = input()
type_room = input()
rate = input()

apartment = 25
room = 18
predident_apartment = 35
discount = 0

if type_room == "apartment":
    if stay_days >= 10:
        discount = (stay_days * apartment) * 0.10
print(discount)