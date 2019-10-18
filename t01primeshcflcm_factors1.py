# What are the factors of 18?

def print_factors(x):
   

   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

# change this value for a different result.
num = 18


print_factors(num)
