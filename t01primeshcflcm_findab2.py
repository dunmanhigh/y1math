# If a and b are integers such that a * b = 18, find the possible values of a + b.

num = 18
b = 1

for a in range (1, num+1):
  if num % a == 0:
    b = int(num / a)
    # print(a)
    # print(b)
    # print("\n")
    print(a+b)
