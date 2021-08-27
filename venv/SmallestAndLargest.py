first = int(input("Enter the First Number"))
second = int(input("Enter the Second Number"))
third = int(input("Enter the Third Number"))

sum = first + second + third
print(sum)
product = first * second * third
print(product)
average = sum / 3
print(average)

if (first < second and first < third):
    print("The first number is the smallest")
if (second < first and second < third):
    print("The second number is the smallest")
if (third < first and third < second):
    print("The third number is the smallest")

if (first > second and first > third):
    print("The first number is the largest")
if (second > first and second > third):
    print("The second number is the largest")
if (third > first and third > second):
    print("The third number is the largest")


