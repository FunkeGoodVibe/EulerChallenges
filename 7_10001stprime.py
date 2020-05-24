# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def prime_count():

    curr_primes = []    #start with no prime numbers in the list

    for n in range(2, 10002):   # ensure the last number is included (!)

        # Assume number is prime until shown it is not.
        isPrime = True

        for num in range(2, n):     #divide current number, by all numbers in range so far.
            if n % num == 0:
                isPrime = False     #if no remainder, then prime
                break

        if isPrime:
            curr_primes.append(n)       #add prime item to list

    print(curr_primes, end = ", ")

prime_count()
