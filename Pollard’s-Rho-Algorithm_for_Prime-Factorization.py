# find a prime factor of composite using Pollard's Rho algorithm

import random
import math

def modular_pow(base, exponent,modulus):
	result = 1
	while (exponent > 0):
		# if y is odd, multiply base with result
		if (exponent & 1):
			result = (result * base) % modulus
		exponent = exponent >> 1
		base = (base * base) % modulus
	return result

# method to return prime divisor for n
def PollardRho( n):
	if (n == 1):
		return n
	if (n % 2 == 0):
		return 2
	x = (random.randint(0, 2) % (n - 2))
	y = x

	# Algorithm can be re-run with a different c
	c = (random.randint(0, 1) % (n - 1))

	d = 1

	# If n is prime, return n
	while (d == 1):
		x = (modular_pow(x, 2, n) + c + n)%n
		y = (modular_pow(y, 2, n) + c + n)%n
		y = (modular_pow(y, 2, n) + c + n)%n
		d = math.gcd(abs(x - y), n)
		if (d == n):
			return PollardRho(n)
	
	return d

if __name__ == "__main__":

	n = 10967535067
	print("One of the divisors for", n , "is ",PollardRho(n))
