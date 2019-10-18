# Is num a prime number? 
# A prime number is an integer with exactly 2 different factors, 1 and itself.
# Can you rectify the following program error?
num = 61



# prime numbers are greater than 1
if num > 1:
 
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       

else:
   print(num,"is not a prime number")
