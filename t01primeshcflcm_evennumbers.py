# What are the even numbers from 1 to num?

num = 123
for i in range(1, num+1):
  if i % 2 == 0:
    print(i, end=' ')
    
# is num odd or even     
num = input("enter number")
if num % 2 == 0:
  print("even")
else:
  print("odd")
