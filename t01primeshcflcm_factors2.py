# Generate a list containing factors of 10.

num = 10

for i in range(1, num+1):  
  if num % i == 0:
    print(i, end=' ')
