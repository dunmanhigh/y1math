# What are the even numbers from 1 to num?

num = 123
for i in range(1, num+1):
  if i % 2 == 0: # when i divided by 2 has no remainder, i is even
    print(i, end=' ') # prints outputs on same line, separated by a space
