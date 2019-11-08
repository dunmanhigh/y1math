# What is the kth term? How do you check it?

k = 10

A = [1, 4, 7, 10, 13, 16, 19] #number pattern
b = A[2] - A[1] #constant difference
c = A[0] - b #0th term

kthterm = b*k - c #kth term

print(kthterm)
