startstr = input("input string ")
startstr = list(startstr)
brack = startstr.count("[") + startstr.count("]")
curl = startstr.count("{") + startstr.count("}")
para = startstr.count("(") + startstr.count(")")
if brack % 2 == 0 and curl % 2 == 0 and para % 2 == 0:
	print("All special characters have a match")
else:
	print("Not all special characters have a match")