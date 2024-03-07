blockamt = int(input("Enter total blocks: "))
counter1 = 0
counter2 = 1
runningtotal = 1
while(runningtotal < blockamt):
	counter2 += 1
	runningtotal = runningtotal + counter2
	if runningtotal < blockamt:
		counter1 += 1
if blockamt == 1:
	blockamt -= 1
counter1 += 1
runningtotal -= counter2
leftovers = blockamt - runningtotal
print(f"{counter1} level(s) with {leftovers} block(s) left over.")