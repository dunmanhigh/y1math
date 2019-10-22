# Find the Highest Common Factor (HCF) of a and b.

def computeHCF(a, b):

    if a > b:
        smaller = b
    else:
        smaller = a
    for i in range(1, smaller+1):
        if((a % i == 0) and (b % i == 0)):
            hcf = i
            
    return hcf

a = int(input("a: "))
b = int(input("b: "))

print(computeHCF(a, b))
