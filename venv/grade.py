userinput = (input('Enter Student Grades'))

A = 90
B = 89 - 80
C = 79 - 70
D = 69 - 55
F = 54
grade = 0


if grade >= 90:
    print('Excellent you succeeded ')

elif grade <= 89 and grade <= 80:
    print('Very good Keep it up ' )

elif grade <= 79 and grade <= 70:
    print('Good Keep Working Harder')

elif grade <= 69 and grade <= 55:
    print('Try Working Harder')

else:
    print('FAilED you will repeat the class ')
