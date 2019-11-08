# Generate a list containing factors of 100.

num = 100

for i in range(1, num+1):  #i interates from 1 to 101
  if num % i == 0:
    print(i, end=' ')
