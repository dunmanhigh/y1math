# Find the difference between the terms

A = [1, 4, 7, 10, 13, 16, 19] # constant difference
print(A[0] - A[6])
for i in range(len(A)-6):
  print(A[i+1] - A[i])
