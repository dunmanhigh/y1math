# Find the Highest Common Factor (HCF) of 18 and 30.

def HCF(x, y):

# choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
            
    return hcf
  
print(HCF(18, 30))
