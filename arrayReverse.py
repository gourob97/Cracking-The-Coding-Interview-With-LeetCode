#   time comlexity O(n)

#   space complexity O(n)


a = [1,2,3,4]

startp = 0
endp = len(a) - 1  

while(startp < endp):
	# temp = a[startp] 
	# a[startp] = a[endp]
	# a[endp] = temp
	a[startp],a[endp] = a[endp], a[startp]
	startp+=1
	endp-=1

print(a)
