# Find the HCF of n positive integers.

def gcd(a, b): 
    while(b): 
        (a, b) = (b, a % b)
    return a
  
numbers = [1, 2, 3, 4, 5] 
num1 = numbers[0] 
num2 = numbers[1]
gcdnum = gcd(num1,num2)
for i in range(2,len(numbers)): 
    gcdnum  = gcd(gcdnum, numbers[i]) 
print(gcd) 
