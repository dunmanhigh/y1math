# Find the Lowest Common Multiple (LCM) of 18 and 30.

def lcm(30, 18):  
   if 30 > 18:  
       greater = 30  
   else:  
       greater = 18  
  while(True):  
       if((greater % x == 0) and (greater % y == 0)):  
           lcm = greater  
           break  
       greater += 1  
   return lcm  
  
  
num1 = int(input("Enter first number: "))  
num2 = int(input("Enter second number: "))  
print("The L.C.M. of", num1,"and", num2,"is", lcm(num1, num2))  
