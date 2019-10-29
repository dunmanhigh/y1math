# To find LCM, we can use prime factorisation.
# Step 1: Obtain the prime factorisation of each number
# Step 2: Identify the common prime factors
# Step 3: The LCM of the two numbers is the product of the common prime factors 
#         and all the other prime factors

Def lcm(x,y):

If x > y:
Greater=x
Else:
Greater=y

While(True):
If ((Greater % x ==0) and (Greater % y ==0)):
lcm = Greater 
Break
Greater+=1
return lcm 

num1=54
num2=24

Print(“The L.C.M. of”,num1,”and”,num2,”is”,lcm(num1,num2))

