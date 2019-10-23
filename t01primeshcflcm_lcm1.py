# Find the Lowest Common Multiple (LCM) of 18 and 30.
# define a function
def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    
    while True:
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    print(lcm)

lcm(18,30)
