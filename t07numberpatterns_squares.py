# Generate squares number pattern from 1 to 10
# 1 4 9 16 25 ...
def printValues():
	l = list()
	for i in range(1,10):
		l.append(i**2)
	print(l)
		
printValues()
