grade = float(input("Enter your grade: "))

if grade == 6.0:
    print("Excellent")
elif grade >= 5.5:
    print("Very Good")
elif grade >= 4.5:
    print("Good")
elif grade >= 3.5:
    print("Average")
elif grade >= 3.0:
    print("Poor")
elif grade < 3.0:
    print("Fail")
else:
    print("Invalid grade")

print("Thanks for using Grade Classifier!")
