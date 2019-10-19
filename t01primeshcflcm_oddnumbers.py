# What are the odd numbers from 1 to num?

print('Odd numbers from 1 to 123')
num = 123
for i in range(1, num+1):
  if i % 2 in range(1, num):
    print(i, end=' ')
