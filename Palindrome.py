import re
x = int(input("Input x: "))
y = int(input("Input y: "))
tally = 0
while x <= y:
	numslist = []
	templist = []
	templist2 = []
	numslist = str(x)
	numslist = list(numslist)
	pointer = 0
	if (len(numslist)) % 2 == 0:
		halfwaypoint = len(numslist) / 2
		while(pointer < halfwaypoint):
			templist.append(numslist[pointer])
			pointer += 1
		while(pointer < len(numslist)):
			templist2.append(numslist[pointer])
			pointer += 1
		templist.reverse()
		if templist == templist2:
			tally += 1
	else:
		halfwaypoint = (len(numslist)) / 2
		halfwaypoint = halfwaypoint -0.5
		while(pointer < halfwaypoint):
			templist.append(numslist[pointer])
			pointer += 1
		pointer += 1
		while(pointer < len(numslist)):
			templist2.append(numslist[pointer])
			pointer += 1
		templist.reverse()
		if templist == templist2:
			tally += 1
	x += 1
print(tally)