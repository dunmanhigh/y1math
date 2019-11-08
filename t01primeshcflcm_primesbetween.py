# What are the prime numbers from 20 to 567?

START = 20
END = 567

for i in range(START-1,END):
  if (2**(i))%(i+1)==0 or i==2 not i==341 not i==561:
    print(i+1)
