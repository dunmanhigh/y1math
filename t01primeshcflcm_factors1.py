# What are the even numbers from 1 to num?

# user to input number
num = int(input('input an interger: '))

# run a loop from 1 to mumber + 1
for i in range(1, num+1):
  # Check if the number is even by checking if the remainder is zero af
  if i % 2 == 0:
    # print all the even numbers in a line
    print(i, end='  ')
