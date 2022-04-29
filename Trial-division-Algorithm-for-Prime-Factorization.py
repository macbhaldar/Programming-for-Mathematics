# Trial Division Algorithm
## Function to check if a number is a prime number or not

def TrialDivision(N):
	i = 2  # Initializing with the value 2
	k = int(N ** 0.5)  # Computing the square root of the number N

	# While loop till the square root of N
	while(i<= k):
		if(N % i == 0):  # If any of the numbers between [2, sqrt(N)] is a factor of N Then the number is composite
			return 0
		i += 1
	return 1  # If none of the numbers is a factor, then it is a prime number

if __name__ == "__main__":
	N = 123
	p = TrialDivision(N)

# To check if a number is a prime or not
	if(p):
		print("Prime")
	else:
		print("Composite")
