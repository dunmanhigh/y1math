# If a and b are integers such that a * b = 17, find the value of a + b.

num = 17



for i in range(1, num+1):  

  if num % i == 0:

    print(i, end=' ')
