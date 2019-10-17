# Generate a list containing factors of num.

num = 123

for i in range(1, num+1):  
  if num % i == 0:
    print(i, end=' ')
