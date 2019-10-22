# Generate multiples of 5 from 1 to 100

START = 5
END = 100
num = 5

for i in range(START, END+1):
  if i % num == 0:
    print(i, end='100 ')
