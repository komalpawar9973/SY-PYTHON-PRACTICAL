print("----customer feedback----". center(70).upper())
name=input("enter your name:".title())
product=input("enter product name:".lower())
feedback= input("enter your feedback:".capitalize())

print("----display feedback -------".center(70).upper())
print("name:",name.upper().rstrip())
print("product name:",product.upper().lstrip())
print("feedback:",feedback.upper().strip())