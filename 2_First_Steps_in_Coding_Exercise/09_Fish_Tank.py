lenght = int(input())
widht = int(input())
hight = int(input())
procent = float(input())

aqarium_value = lenght * widht * hight
value_liters = aqarium_value / 1000
needed_liters = value_liters * (1 - procent / 100)
print(needed_liters)