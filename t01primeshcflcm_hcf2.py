# Find the Highest Common Factor (HCF) of a and b.

x = int(input("x: "))
y = int(input("y: "))
if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
            
