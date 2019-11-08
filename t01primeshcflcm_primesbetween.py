# What are the prime numbers from 20 to 567?

START = 20
END = 567
print("Prime numbers between",START,"and",END,"are:")

for num in range(START,END + 1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)

