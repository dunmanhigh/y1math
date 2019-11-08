# What is the kth term? How do you check it?

k = 10

A = [1, 4, 7, 10, 13, 16, 19] # constant difference

#answer:

print(k * (A[1] - A[0]) + A[0])

#take constant difference times k plus first number in list
