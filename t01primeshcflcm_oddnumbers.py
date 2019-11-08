# What are the odd numbers from 1 to num?

num = 123
for i in range(1, num+1):
  if i % 2 == 1: # or != 0
    print(i, end=' ')
    
   #is num an odd number
num=int(input("enter a number"))
if num % 2 == 1 :
  print("yes")
else :
  print("no")
