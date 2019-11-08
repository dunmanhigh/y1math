# Generate oscillating pattern 1, -1, 1, -1, 1, -1, ... k times

k = 10

for i in range(k):
  if i % 2 == 0:
    print("-1")
  else:
    print("1")
    
  
