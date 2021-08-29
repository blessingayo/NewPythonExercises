number = int(input())


def factorial(number):
    if number <= 0:
        return 1
    else:
        return factorial(number - 1) * number


print(factorial(6))


def factorials(numbers):
    if numbers <= 0:
        return 1
    else:
        multiply = factorials(numbers - 1) * numbers
    print(numbers, "* ", numbers - 1, "= ", multiply)
    return multiply


factorials(6)
