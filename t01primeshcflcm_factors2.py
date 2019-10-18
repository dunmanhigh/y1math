# Generate a list containing factors of num.

num = 10
factor = []
for i in range(1,num+1):
  if num % i == 0:
    factor.append(i)
print(factor)
[1, 2, 5, 10]
