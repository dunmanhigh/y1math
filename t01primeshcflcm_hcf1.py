# Find the Highest Common Factor (HCF) of 18 and 30.

num1 = 3
num2 = 9
b = 0

for i in range(1,num1+1):
  if num1 % i == 0:
    for j in range(1,num2+1):
      if num2 % j == 0:
        if i == j:
          print (i)
