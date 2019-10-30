# The process of expressing a number as a product of its prime factors is called prime factorisation.
# Express 18 as a prime factorisation.

n = 18
i = 2

while i * i < n:
    while n%i == 0:
        n = n / i
    i = i + 1

print (n)
