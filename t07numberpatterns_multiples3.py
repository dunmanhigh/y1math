# Generate multiples of 3 from 1 to 50

START = 5
END = 890
num = 9

for i in range(START, END+1):
  if i % num == 0:
    print(i, end=' ')
