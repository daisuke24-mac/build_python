def pattern(n):	
	for i in range(0, n):
		for j in range(1, i+2):
			print('{}'.format(j))
	for i in range(n,1,-1):
		for j in range(1,i):
			print(j)
pattern(4)
		