# Is num a prime number? 
# A prime number is an integer with exactly 2 different factors, 1 and itself.
# Consider implementing stop checking at int(num ** 0.5) for efficiency.

num = 61

listoffactors=[]
for i in range(1, num+1):  
  if num % i == 0:
    listoffactors.append(i)
if listoffactors[0]==1 and listoffactors[1]==num:
  print("num is a prime")
else:
  print("num is not a prime")
