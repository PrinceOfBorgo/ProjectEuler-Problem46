# coding=utf-8
from math import sqrt
from getopt import getopt
from sys import argv
import colorama


# Naive method to discover if a number is prime.
def isprime(n):
    # The only primes less than or equal to 3 are 2 and 3.
    if n <= 3:
        return n > 1
    # Otherwise, if the number is divisible by 2 or 3 it is not prime.
    elif (n % 2 == 0) or (n % 3 == 0):
        return False
        
    # Starting from 5, prime numbers are all of the form 6*m ± 1 (viceversa is
    # false! e.g. 25 = 6*4+1 and it is not prime).
    # We can loop through all the numbers k = 6*m ± 1 until we find a divisor
    # of n.
    # We can contrain k to be less than or equal to sqrt(n) since the next
    # values have been checked previously.
    k = 5
    while k * k <= n:    # While k <= sqrt(n) ...
        # If (6*m + 1) or (6*m - 1) is a divisor of n, then n is not prime.
        if (n % k == 0) or (n % (k + 2) == 0):
            return False
        k += 6      # Find the next 6*m ± 1 couple.
        
    # If we get here, then we have not found any non-trivial divisor for n so
    # it is prime.
    return True

###############################################################################


### SETUP CROSS-PLATFORM COLORED TEXT ###

# Colors.
CEND    = "\033[00m"
CGRAY   = "\033[30m\033[01m"
CRED    = "\033[31m\033[01m"
CGREEN  = "\033[32m\033[01m"

# Enable colored text.
colorama.init()



### CHECK OPTIONS ###

# Verbose mode.
opts, args = getopt(argv[1:], "v", ["verbose"])
verbose = False
for opt, arg in opts:
    verbose = opt in ("-v", "--verbose")



### START PROGRAM ###

# We want to check if 2*n + 1 = p + 2*k^2 with p prime.
n = 1
while True:
    # Case p = 3:
    #   If we can write 2*m + 1 as 3 + 2*k^2, this number verifies the
    #   conjecture so we check the next odd number to find the counterexample.
    if sqrt(n - 1) % 1 == 0:
        if verbose:
            print("%s%d %s( = 3 + 2 * %d )" %(CRED, 2*n+1, CGRAY, n-1))
        n += 1
        continue    # Restart the while loop with the next odd number.
    
    # Case p = 6*m ± 1 :
    #   1) If we can write 2*m + 1 as p + 2*k^2 with p = 6*m ± 1, then we must
    #      check if p is prime:
    #       a) If p is prime then 2*m + 1 verifies the conjecture so we check
    #          the next odd number to find the counterexample.
    #       b) Else if p is not prime we check the next p = 6*m ± 1.
    #   2) Else if we cannot write 2*m + 1 as p + 2*k^2 with p = 6*m ± 1, then
    #      we must check the next p = 6*m ± 1.
    done = True
    for m in range(1, (n+1)//3 + 1):
        x = n - 3*m
        
        # If 2*m + 1 = 6*m + 1 + 2*k^2, then p = 6*m + 1.
        if x >= 0 and sqrt(x) % 1 == 0:
            p = 6*m + 1
        # If 2*m + 1 = 6*m - 1 + 2*k^2, then p = 6*m - 1.
        elif sqrt(x + 1) % 1 == 0:
            p = 6*m - 1
            x = x + 1   # Replace x with x + 1 for formatting purposes
                        # (see next "if" block: "if isprime(p): ...").
        # Else 2*m + 1 != p + 2*k^2 so we must check the next p = 6*m ± 1.
        else:
            continue
        
        # If p is prime, then 2*m + 1 verifies the conjecture so we must check
        # the next odd number to find the counterexample
        # (set done to False and break the for loop).
        if isprime(p):
            if verbose:
                print("%s%d %s( = %d + 2 * %d )" %(CRED, 2*n+1, CGRAY, p, x))
            done = False
            break
    # If done is True this means that we have not found any prime p that
    # satisfies 2*m + 1 = p + 2*k^2, so we found the least counterexample to
    # the conjecture.
    if done:
        break
    # Otherwise keep searching.
    else: 
        n += 1

# The result is finally printed.
if verbose:
    print()
print("%sCounterexample found! %s%d" %(CEND, CGREEN, 2*n + 1))