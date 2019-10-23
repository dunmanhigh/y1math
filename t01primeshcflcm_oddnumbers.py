# What are the odd numbers from 1 to num?

num = 123

lower_limit = int(input("Enter the lower limit : 1"))
upper_limit = int(input("Enter the upper limit : 123"))

for i in range(lower_limit,upper_limit + 1):
    #3
    if(i%2 != 0):
        print("{} ".format(i))
 
