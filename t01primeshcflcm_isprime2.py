# Is num a prime number? 
# A prime number is an integer with exactly 2 different factors, 1 and itself.
# Can you rectify the following program error?

num = 61

prime = True
for i in range(2,num): # won't work for 2 which is the only even prime
  if num % i == 0:
    prime = False
  
print(prime)
num = 407
= int(input("Enter a number: "))

# prime numbers are greater than 1
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")
# take input from the user
# num 
