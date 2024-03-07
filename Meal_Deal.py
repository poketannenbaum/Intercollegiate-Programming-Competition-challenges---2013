import re
trav = float(input("Enter number of travelers: "))
bills = input("Enter daily food bills: ")
bills = re.split(" ", bills)
bills = list(map(float, bills))
avg = 0
for num in bills:
	avg += num
avg = avg / len(bills)
repay = 0
for num in bills:
	if num < avg:
		repay += avg - num
print(repay)