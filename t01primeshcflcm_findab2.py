# If a and b are integers such that a * b = 18, find the possible values of a + b.

num = 18
a = 1
for a in range(1, num):
    b = num % a
    if b == 0:
      print("a: {}, b: {}, a+b: {}".format(a, b, a+b))
