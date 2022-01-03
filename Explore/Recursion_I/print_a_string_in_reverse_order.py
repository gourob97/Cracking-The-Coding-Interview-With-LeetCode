
def reversePrint(str):
	if len(str) == 0:
		return
	
	
	reversePrint(str[1:])
	print(str[0],end="")


inp = input()
reversePrint(inp)

