# Craft your question and code your solution ~
# Contributed by V Lew    Level of difficulty (year 1s) : Basic to Intermediate
#
# Objective - 
# Allow student to use Year 1 math knowledge to find the general term.
# Then learn to use the for loop structure and variable i, and print() syntax, 
# and basic math expressions including add/subtract(+/-), multiply(*)  
# and power(exponentiation **) to generate the required number patterns.
# Anticipate students to do trial and error approach in forming the general term.
#
# The first 7 terms of a number sequence: 3 7 11 15 19 23 27	
# Write Python code using a for loop to print out the above number sequence.

for i in range(7):  
    num = 4 * (i+1) - 1
    print(num, end=' ')

# Alternate solution:

for i in range(1, 8):
  print(4 * i - 1, end=' ')


# Repeat the above for the number sequence below
# 2 8 18 32 50 72 98




# Repeat the above for the number sequence below
# 0 3 8 15	24 35	48
