# Implement the Sieve of Erathosthenes for numbers between 1 to 100.
 
def SieveOfEratosthenes(100): 
      
    # Create a boolean array "prime[0..n]" and initialize 
    # all entries it as true. A value in prime[i] will 
    # finally be false if i is Not a prime, else true. 
    prime = [True for i in range(101)] 
    p = 2
    while (p * p <= 101): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
              
            # Update all multiples of p 
            for i in range(p * 2, 101, p): 
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    # Print all prime numbers 
    for p in range(101): 
        if prime[p]: 
            print p, 
