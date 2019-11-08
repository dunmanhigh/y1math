# What are the factors of 20?
# factor: an integer which when multiplied with another integer, results in the product 18. 
# Hence when 18 is divided by this number, the dividend is an integer and there are no remainders.

num = 20

for i in range(1, num+1):  
  if num % i == 0:
    print(i, end=' ')
