# Find the highest common factor (HCF) of 3 numbers a, b and c.

a = 4
b = 5
c = 7
# Python program to find the H.C.F of two input number

# define a function
def computeHCF(x, y):

# choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
            
    return hcf
  
  
 def computeHCFtwo(x, y):

# choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
            
    return hcf

num1 = 4
num2 = 5
num3 = 7


# take input from the user
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

print("The H.C.F. of", num1,"and", num2,"is", computeHCF2(computeHCF(num1, num2), num3))
