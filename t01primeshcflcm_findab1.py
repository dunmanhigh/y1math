# If a and b are integers such that a * b = 17, find the value of a + b.

num = 17
listoffactors=[]
for i in range(1, num+1):  
  if num % i == 0:
    listoffactors.append(i)
print(listoffactors[0]+listoffactors[1])
