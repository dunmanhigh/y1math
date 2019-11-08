# Find the Highest Common Factor (HCF) of a and b.

a = int(input("a: "))
b = int(input("b: "))

def hcfnaive(a,b): 
    if(b==0): 
        return a 
    else: 
        return hcfnaive(b,a%b) 
  
print ("The gcd of " a " and " b " is" : ",end="") 
print (hcfnaive(a,b))
