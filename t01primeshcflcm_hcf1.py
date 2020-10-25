# Find the Highest Common Factor (HCF) of 18 and 30.
a = 18
b = 30

while b != 0:
    (a, b) = (b, a % b)
print(a)
