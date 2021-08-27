milesDriven = 0
gallonUsed = 0
milesPerGallon = 0
total = 0

while (milesDriven != -1 and gallonUsed != -1):
    milesDriven = float(input("Enter Your Miles Driven: "))
    if (milesDriven != -1):
        gallonUsed = float(input("Enter Your gallon Used: "))
        if (gallonUsed != -1):
            milesPerGallon = (milesDriven * 1.0) / gallonUsed
            print("Your Miles Per Gallon ", milesPerGallon)

print("Total is ", total)
print(f"Total is {total}")

