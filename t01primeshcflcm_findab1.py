# If a and b are integers such that a * b = 17, find the value of a + b.

# a = 1 so b= a -1
# a = 2 so b = a -2
# if a is < b, continue. 

c = 0
a = 1
b = 18/a

while a<=b:
  c = a+b
  if b == int(b):
    #print(str(a)+":" +str(b)+":" +str(c), end=' ')
    print(str(c), end=' ')
  a = a+1
  b= 18/a
