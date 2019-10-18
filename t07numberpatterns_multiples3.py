# Generate multiples of 3 from 1 to 50

START = 1
END = 50
num = 3

for i in range(START, END+1):
  if i % 3 == 0:
    print(i, end=' ')
