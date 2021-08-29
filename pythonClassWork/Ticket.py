ticket = (input("Enter any six digit"))
sum_of_first_three = 0
sum_of_last_three = 0
for i in range(3):
    sum_of_first_three += int(ticket[i])

for i in range(3, 6):
    sum_of_last_three += int(ticket[i])

if sum_of_first_three == sum_of_last_three:
    print("lucky")
else:
    print("ordinary")

#     another way of solving this question

ticket = input()
numbers_int = [int(num) for num in ticket]
print("lucky" if sum(numbers_int[0 : 3]) == sum(numbers_int[3 : 6]) else "ordinary")