# What are the odd numbers from 1 to num?

num = 123
for i in range(1, num+1):
  if i % 2 == 1: # or != 0
    print(i, end=' ')
# Python program to print odd Numbers in given range 
  
start, end = 4, 19
  
# iterating each number in list 
for num in range(start, end + 1): 
      
    # checking condition 
    if num % 2 != 0: 
        print(num, end = " ") 
