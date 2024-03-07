import re
seriessize = input("Numbers in series ")
subsize = int(input("Size of subset "))
nums = input("Numbers in series ")
nums = re.split(" ", nums)
nums = list(map(float, nums))
ogsub = subsize
avgarr = []
avg = 0
point = 0
count = 0
while(True):
	try:
		while point < subsize:
			avg += nums[point]
			point += 1
		count += 1
		avg = avg / ogsub
		avgarr.append(avg)
		subsize += 1
		point = count
		avg = 0
	except:
		break
print(avgarr)