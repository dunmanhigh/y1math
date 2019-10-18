# Generate a list containing factors of num.
num = input() #take in num from input
factors = []

for i in range(1, num+1):
  if num % i == 0:
      factors.append(i)

print(factors)
