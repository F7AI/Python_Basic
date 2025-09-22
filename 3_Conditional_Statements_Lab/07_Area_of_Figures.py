import math

command = input()

if command == "square":
    side = float(input())
    area = side ** 2
    print(f"{area:.3f}")

elif command == "rectangle":
    length = float(input())
    width = float(input())
    area = length * width
    print(f"{area:.3f}")

elif command == "circle":
    radius = float(input())
    area = math.pi * (radius ** 2)
    print(f"{area:.3f}")

elif command == "triangle":
    base = float(input())
    height = float(input())
    area = 0.5 * base * height
    print(f"{area:.3f}")

else:
    print("Unknown command")