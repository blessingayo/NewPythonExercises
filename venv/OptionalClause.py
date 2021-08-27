for i in range(2):
    value = int(input('Enter a number (press -1 to break): '))
    print('You entered:' , value)

    if value == -1:
        break

else:
    print('Theloop terminated without executing the break')