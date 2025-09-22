page_number = int(input())
reading_per_hour = int(input())
days_for_reading = int(input())

oll_time_dayly_reading = page_number / reading_per_hour
needed_time_dayly = oll_time_dayly_reading // days_for_reading
print(needed_time_dayly)
