# Find the Highest Common Factor (HCF) of 18 and 30.

a=18
b=30
c=1

c=min(a,b)


d=c
while (d>0):
  if (a % d==0) and (b % d==0):
    print (d)
    break
  else:  d = d-1
end
