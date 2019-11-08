# Is num a composite number? 
# A composite number is an integer with more than 2 different factors / is a product of at least 2 primes.

num = 63
num_factors = 0
for i in range(1,num+1):
  if num % i == 0:
    num_factors += 1
if num_factors > 2:
  print(num, "is composite")
else:
  print(num, "is not composite") 
