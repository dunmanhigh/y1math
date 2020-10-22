# Generate oscillating pattern 1, -1, 2, -2, 3, -3, ... k times

k = 10
num = 1

for i in range(1, k+1):
  if i % 2 == 1:
    num = num-(i+1)
    print(num)
  if i % 2 == 0:
    num = num+(i+1)
    print(num)
