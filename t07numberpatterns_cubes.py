# Generate cubes number pattern from 1 to 10
# 1 8 27 64 ...

num = 1
where num < 11:
  cube = num * num * num
  print(cube)
  num = num + 1
