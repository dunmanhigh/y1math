# What are the even numbers from 1 to num?

# number is 123
num = 123

# loop from 1 to num (syntax num+1 at the end)
for i in range(1, num+1):
  # test if even (remainder after dividing by 2 is 0
  if i % 2 == 0:
    # printout, in same line
    print(i, end=' ')
