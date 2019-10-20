# The process of expressing a number as a product of its prime factors is called prime factorisation.
# Express 18 as a prime factorisation.
import sympy as smp

try:
    number = int(input('Enter a number : '))
except(ValueError) :
    print('Please enter an integer !')
num = number
prime_factors = []
if smp.isprime(number) :
    prime_factors.append(number)
else :
    for i in range(2, int(number/2) + 1) :   
        if smp.isprime(i) and number % i == 0 :
            while(number % i == 0) :
                prime_factors.append(i)
                number = number  / i
print('prime factors of ' + str(num) + ' - ')
for i in prime_factors :
    print(i, end = ' ')

