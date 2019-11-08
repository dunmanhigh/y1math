# Find the highest common factor (HCF) of 3 numbers a, b and c.
q=0
a = int(input('First number'))
b = int(input('Second number'))
c = int(input('Third number'))
while a%q!=0 and b%q!=0 and c%q!=0:
  q+=1
print(q)
