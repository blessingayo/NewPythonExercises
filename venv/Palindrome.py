userinput = int(input('Enter any 5 numbers at once: '))
number = 0
firstNumber = number / 10000
newNumber = number % 10000
secondNumber = number / 1000
number1 = newNumber % 1000
thirdNumber = number /100
number2 = newNumber % 100
forthNumber = number / 10
number3 = newNumber % 10
fifthNumber = number / 1

palindrome = firstNumber == thirdNumber

if palindrome:
    print("It is palindrome%n ", fifthNumber, forthNumber, thirdNumber, secondNumber, firstNumber)

else:
    print(" It is not palindrome%n ", fifthNumber, forthNumber, thirdNumber, secondNumber, firstNumber)