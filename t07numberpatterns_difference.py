# Find the difference between the terms

A = [2, 4, 6, 8, 10, 12, 14] # constant difference
print(A[1] - A[0])
for i in range(len(A)-1):
  print(A[i+1] - A[i])
