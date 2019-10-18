# What is the prime number greater than num?

num = int(input("num: "))
theNum = num
something = True
while something:
  theNum += 1
  if (theNum % 1 == theNum) and (theNum % theNum == 1):
    for i in range(2, theNum):
      if theNum % i == 0:
        theNum += 1
      else:
        something = False
print("the prime number greater than num is \(theNum)")
