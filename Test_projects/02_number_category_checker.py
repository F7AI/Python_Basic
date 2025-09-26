number = int(input("Enter a number: "))

# Проверка за положително / отрицателно / нула
if number > 0:
    print("Positive number")
elif number == 0:
    print("Zero")
else:
    print("Negative number")

# Проверка за четно / нечетно
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

