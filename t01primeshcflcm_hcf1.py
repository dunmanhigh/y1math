# Find the Highest Common Factor (HCF) of 18 and 30.
num1 = int(input("Enter first number: "))         
    
num2 = int(input("Enter second number: "))              
hcf = 1
for i in range(min(num1,num2),0,-1):                    
    if (num1%i) == 0 and (num2%i) == 0:
        hcf = i
        break
    
print(hcf)
