# Generate a list containing factors of 1000.

num = 1000

for i in range(1, num+1):  
  if num % i == 0:
    print(i, end=' ')
