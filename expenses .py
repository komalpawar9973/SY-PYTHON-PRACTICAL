print("**** Expenses ****")

expenses = 0.0
food = 0.0
shopping = 0.0
travelling = 0.0
other = 0.0
while True:
    value = float(input("Enter your amount (-1 to stop): "))
    if value == -1:
        break
    category = input("Enter your category (food/shopping/travelling/other): ").lower()
    if category == "food":
        food += value
    elif category == "shopping":
        shopping += value
    elif category == "travelling":
        travelling += value
    else:
        other += value
    expenses += value
print("\n=== Expenses Summary ===")
print("Food:", food)
print("Shopping:", shopping)
print("Travelling:", travelling)
print("Other:", other)
print("Total Expenses:", expenses)

