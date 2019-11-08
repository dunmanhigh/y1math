# Find the highest common factor (HCF) of 3 numbers a, b and c.

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

def hcf(x, y, z):

# choose the smaller number
    if x < y and z:
        smaller = x
    elif y < x and z:
        smaller = y
    else:
        smaller = z
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
            
    return hcf
 
print(hcf(a, b, c))
