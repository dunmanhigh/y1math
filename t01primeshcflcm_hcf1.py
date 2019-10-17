# Find the Highest Common Factor (HCF) of 18 and 30.
num = 18

for i in range(1, num+1):  
  if num % i == 0:
    print(i, end=' ')
num = 30

for i in range(1, num+1):  
  if num % i == 0:
    print(i, end=' ')
