age = int(input("Please enter your age (years): "))
weight = int(input("Please enter your weight (kg): "))

if age > 12 and weight > 40:
    print("Recommended: 1-2 pills")
elif 7 <= age <= 12 and 26 <= weight <= 40:
    print("Recommended: 1/2 - 1 pill")
elif 3 <= age <= 7 and 15 <= weight <= 25:
    print("Recommended: 1/2 pill")
else:
    print("No recommendation available for the given age and weight.")
