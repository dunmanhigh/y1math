# What are the even numbers from 1 to num?

# User to input number
num = int(input('Input an integer:'))

# Run a loop from 1 to number + 1 
for i in range(1, num+1):
  # Check if the number is even by checking if the remainder zero is af
  if i % 2 == 0:
    # print all even numbers in a line
    print(i, end=' ')
