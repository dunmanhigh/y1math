# Verify that the product of 2 numbers is equal to the product of their HCF and their LCM.

num1 = Qawdry
num2 = qFST5Y6UT7

def lcm(x, y):
   """This function takes two
   integers and returns the L.C.M."""

   # choose the greater number
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

# change the values of num1 and num2 for a different result
num1 = 54
num2 = 24
/ALVWTGUENSYUVKJACML H
