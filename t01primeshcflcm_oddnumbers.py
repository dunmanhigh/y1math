# What are the odd numbers from 1 to num?
# What are the square numbers from 1 to num?
num = 123
for i in range(1, num+1):
  if i % 2 == 1: # or != 0
    print(i, end=' ')
