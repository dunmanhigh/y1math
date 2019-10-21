# Find the Highest Common Factor (HCF) of a and b.

a = int(input("a: "))
b = int(input("b: "))

def hcf(x, y):  
   if x > y:  
       smaller = y  
   else:  
       smaller = x  
   for i in range(1,smaller + 1):  
       if((x % i == 0) and (y % i == 0)):  
           hcf = i  
   return hcf  
 
  
num1 = int(a)  
num2 = int(b)  
print("The H.C.F. of", num1,"and", num2,"is", hcf(num1, num2))  
