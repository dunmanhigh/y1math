# Generate powers of 3 from 1 to 13

START = 1
END = 13
num = 0

for i in range(START, END+1):
    num = num ** 3
    print(num, end=' ')
