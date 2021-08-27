x = float(input("Enter any positive or negative number"))
y = float(input("Enter another positive or negative number"))

if x == 0 and y == 0:
    print("it's the origin")
elif x == 0 or y == 0:
    print("One of the coordinate is equal to zero")
elif x >= 0 or y >= 0:
    print("I")
elif x <= 0 or y <= 0:
    print("III")
else:
    print("II")






