hours = int(input())
minutes = int(input())

hours = hours * 60
all_minutes = hours + minutes + 15
hour = all_minutes // 60
hour = hour % 24
minute = all_minutes % 60
print(f'{hour}:{minute:02d}')

