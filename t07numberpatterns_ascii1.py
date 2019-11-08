# Find the ASCII value of 'A' to 'Z'
# http://www.asciitable.com/
START: A
END: Z
for i in range(26):
  print(ord('A') + i, end=' ')

