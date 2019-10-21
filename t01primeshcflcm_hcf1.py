# Find the Lowest Common Multiple of 20 and 5
# Lowest Common Multiple is the smallest number that can be divided by both numbers.
a=20
b=5
while a%b==0:
  c=a/b
  break
ans=b*c
print(ans)
