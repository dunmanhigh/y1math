# Generate a list containing factors of num.

num = 20

for i in range(1, num+1): # 1 to 20
   if num % i == 0:
    print(i, end=' ')
