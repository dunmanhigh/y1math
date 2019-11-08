# Generate a list containing factors of 100.

num = 100

def print_factors(num):

 for i in range(1, num + 1):
  if num % i == 0:
    print(i)

print_factors(num)
