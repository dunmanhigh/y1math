# Implement the Sieve of Erathosthenes for numbers between 1 to 100.

nums = [i for i in range(1,101)]
def prime_eratosthenes(n):
    prime_list = []
    for i in range(2, n+1):
        if i not in prime_list:
            print (i)
            for j in range(i*i, n+1, i):
                prime_list.append(j)

print(prime_eratosthenes(100))';

