#project euler, problem 10

def sieve(n):
	"""
	finds all primes smaller than n
	using the sieve of eratosthenes
	"""

	primes_dict = {}
	for i in range(2,n):
		primes_dict[i] = True
	p = 2

	while p**2 < n:
		start = p**2 -p
		# print 'start',start
		while start < n:
			new = start + p
			primes_dict[new] = False
			# print 'discredit',new
			start = new
		found_next_p = False
		next_p = int(p)
		while (not found_next_p) and (next_p < n):
			next_p = next_p + 1
			if primes_dict[next_p] == True:
				p = next_p
				# print 'found',p
				found_next_p = True

	primes_list = [key for key,value in primes_dict.items() if value]
	return primes_list

primes_list = sieve(100)
print primes_list
print sum(primes_list) # let's test it out. these two sums should be the same.
print sum([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])