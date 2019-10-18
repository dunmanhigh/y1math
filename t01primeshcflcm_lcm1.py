# Find the Lowest Common Multiple (LCM) of 18 and 30.
def lcm(x, y):
   

   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm


num1 = 18
num2 = 30


print("The L.C.M. of", num1,"and", num2,"is", lcm(num1, num2))
