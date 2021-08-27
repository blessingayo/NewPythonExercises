"""print('{:>10s} is {:<10d}years old.'.format('Bill', 25))"""

print("    {:10s} |   {:2s} |    {:4s}".format("number", "square", "cube "))
for i in range(6):

    print('-------------------------------------')
    print("{:10d} |    {:2d}  |   {:4d}     |" .format(i,i**2,i**3))
