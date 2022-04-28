# Python code for Pollard p-1 (factorization Method)
## Pollard p-1 algorithm is a better approach to find out prime factors of any integer. 
## Using the combined help of Modular Exponentiation and GCD, it is able to calculate all the distinct prime factors.

# importing "math" for calculating GCD
import math

# importing "sympy" for checking prime
import sympy

	
# function to generate prime factors
def pollard(n):
	a = 2  # defining base
	i = 2  # defining exponent

	# iterate till a prime factor is obtained
	while(True):
		a = (a**i) % n  # recomputing a as required
		d = math.gcd((a-1), n)  # finding gcd of a-1 and n using math function

		# check if factor obtained
		if (d > 1):
			return d
			break
		i += 1  # else increase exponent by one for next round

# Driver code
n = 2993
num = n   # temporarily storing n
ans = []  # list for storing prime factors

# iterated till all prime factors are obtained
while(True):
	d = pollard(num)
	ans.append(d)  # add obtained factor to list
	r = int(num/d)  # reduce n
	# check for prime using sympy
	if(sympy.isprime(r)):
		ans.append(r)
		break
	# reduced n is not prime, so repeat
	else:
		num = r
print("Prime factors of", n, "are", *ans)
