world_record = float(input())
range_in_meters = float(input())
time_in_seconds_1m = float(input())

ivan_must_swim = range_in_meters * time_in_seconds_1m
delay = (range_in_meters // 15) * 12.5
total_time = ivan_must_swim + delay

if total_time < world_record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    diff = total_time - world_record
    print(f"No, he failed! He was {diff:.2f} seconds slower.")