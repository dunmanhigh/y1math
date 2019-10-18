# What are the even numbers from 1 to num?

#num is 123
num = 123

#execute a loop from 1 to 123
for i in range(1, num+1):
  #check if the current number is divisible by 2
  if i % 2 == 0:
    #print out the number, in the same line
    print(i, end=' ')
