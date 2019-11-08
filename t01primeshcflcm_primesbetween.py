# What are the prime numbers from 20 to 567?

START = 20
END = 567

for i in range(START, END + 1):
  if i > 1:
    for n in range(2, i):
      if i % n == 0:
        break
      else:
        print(i)

