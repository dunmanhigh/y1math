START = 1
END = 1000
num = 3

for i in range(START, END+1):
  if i % num == 0:
    print(i, end=' ')
