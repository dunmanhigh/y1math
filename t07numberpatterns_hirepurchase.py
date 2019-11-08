# Craft your question and code your solution ~
# Contributed by V Lew. Level of difficulty (year 1s) : Basic
#
# Objective:
# Give students opportunity to examine their own understanding of hire purchase
# calculations and use the basic math functions and learn to use variables
# to create formulae (algebraic representation) to do the mundane calculations
# automatically.
#
# Write Python code that calculate the monthly installments and total 
# amount (including interest) paid for a hire purchase item, that include
# inputs: cost c (in SGD$), downpayment d (in percentage), interest rate r  
# (in percentage) and repayment period t (in years)
# outputs: monthly instalments p (in SGD$), total amount M (in SGD$)
# Eg Inputs: c = 800, d = 20, r = 5, t = 2.  
# Outputs: p and M
c = 800, d = 20, r = 5, t = 2
M == 0.01*d*c+0.01*(100-d)*c*(100+r)*0.01*t
p == M/t*12

# Extend the program to accept inputs from user to calculate the outputs p and M.
