# If a and b are integers such that a * b = 18, find the possible values of a + b.

for a in range (1,19):
  for b in range (1, 19):
    if a * b == 18:
      print(a + b)
