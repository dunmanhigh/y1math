# Generate oscillating pattern 1, -1, 1, -1, 1, -1, ... k times

k = 10

for i in range(1,k+1):
  if i%2==0:
    if i==k:
      print("-1", end=" ")
    else:
      print("-1", end=", ")
  else:
    if i==k:
      print("-1", end=" ")
    else:
      print("1", end=", ")
  
