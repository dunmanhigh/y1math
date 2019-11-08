# Is num a prime number? 
# A prime number is an integer with exactly 2 different factors, 1 and itself.
# Consider implementing stop checking at int(num ** 0.5) for efficiency.

num = 61
num = 61

prime = True
for i in range(2,num): # won't work for 2 which is the only even prime
  if num % i == 0:
    prime = False
  
print(prime)
