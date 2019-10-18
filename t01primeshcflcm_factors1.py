# What are the factors of 18?
# factor: an integer which when multiplied with another integer, results in the product 18. 
# Hence when 18 is divided by this number, the dividend is an integer and there are no remainders.

num = 18

for i in range(1, num+1):  
  if num % i == 0:
    print(i, end=' ')
# Python Program to find the factors of a number

# define a function
def print_factors(x):
   # This function takes a number and prints the factors

   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

# change this value for a different result.
num = 320

# uncomment the following line to take input from the user
#num = int(input("Enter a number: "))

print_factors(num)
