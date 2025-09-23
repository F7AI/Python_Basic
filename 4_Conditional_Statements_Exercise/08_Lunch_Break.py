import math

serial = input()
episode_time = float(input())
time_out = float(input())

lunch_time = time_out / 8
rest_time = time_out / 4
left_time = time_out - lunch_time - rest_time

if left_time >= episode_time:
    time_left = math.ceil(left_time - episode_time)
    print(f"You have enough time to watch {serial} and left with {time_left} minutes free time.")
else:
    time_needed = math.ceil(episode_time - left_time)
    print(f"You don't have enough time to watch {serial}, you need {time_needed} more minutes.")
