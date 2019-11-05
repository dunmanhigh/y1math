# If a and b are integers such that a * b = 17, find the value of a + b.

num = 18
b = 1

for a in range (1, num+1):
  if num % a == 0 and num % b == 0:
    print(a,end=' ')
