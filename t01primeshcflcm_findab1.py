# If a and b are integers such that a * b = 17, find the value of a + b.

num = 17
factors = []

for i in range(1, num+1):  
  if num % i == 0:
    factors.append(i)
    
aplusb = factors[0] + factors[1]
print("a + b = " + str(aplusb))

