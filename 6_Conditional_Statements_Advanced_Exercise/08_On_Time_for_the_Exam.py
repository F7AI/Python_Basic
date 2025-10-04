exam_hours = int(input())
exam_minutes = int(input())
entrance_hours = int(input())
entrance_minutes = int(input())

# Превръщаме всичко в минути
exam_total = exam_hours * 60 + exam_minutes
entrance_total = entrance_hours * 60 + entrance_minutes

diff = entrance_total - exam_total  # + значи закъснял, - значи по-рано

if diff > 0:
    print("Late")
    hours = diff // 60
    minutes = diff % 60
    if hours > 0:
        print(f"{hours}:{minutes:02d} hours after the start")
    else:
        print(f"{minutes} minutes after the start")
elif diff == 0 or abs(diff) <= 30:
    print("On time")
    if diff != 0:  # ако е малко по-рано, но в рамките на 30 мин
        print(f"{abs(diff)} minutes before the start")
else:
    print("Early")
    hours = abs(diff) // 60
    minutes = abs(diff) % 60
    if hours > 0:
        print(f"{hours}:{minutes:02d} hours before the start")
    else:
        print(f"{minutes} minutes before the start")
