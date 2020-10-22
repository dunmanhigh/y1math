# What are the even numbers from 1 to num?
try:
  num = int(input("enter a number")) + 1
except ValueError:
  print("input an integer")
else:
  for i in range(1, num):
    if i % 2 == 0:
      print(i, end='')
