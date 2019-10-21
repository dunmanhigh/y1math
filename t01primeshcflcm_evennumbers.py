# What are the even numbers from 1 to num?

# number chosen is 123
num = 123

# loop from 1 to 123
for i in range(1, num+1):
  # check if after dividing by 2, the remainder is 0?
  if i % 2 == 0:
    # display if so, in the same line
    print(i, end=' ')
