# Find the Highest Common Factor (HCF) of a and b.

a = int(input("a: "))
b = int(input("b: "))

def HCF(x, y):
    HCF = 1
    
    if x % y == 0:
        return y
    
    for k in range(int(y / 2), 0, -1):
        if x % k == 0 and y % k == 0:
            HCF = k
            break  
    return HCF

print(HCF(a, b))

