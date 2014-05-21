#12.py

"""
find the first triangular number with over 500 divisors
hmmm

notes: this is inefficient, should be finding prime factors maybe?
"""

def generate_tri(n):
	"""
	generates n triangle numbers
	"""
	triangles = [0]
	for i in range(1,n):
		triangles.append(i + triangles[i - 1])
	return triangles

def find(n):
	"""
	finds first triangular number with over n divisors
	"""
	triangles = generate_tri(n*100) #arbitrary upper bound for searching

	i = 1
	divisors = {1:set([1])}

	num = triangles[i]
	while len(divisors[num]) <= n:
		num = triangles[i]
		# print i,num
		divisors[num] = set([1,num])
		start = 2
		end = num/2
		while start < end:
			if num % start == 0:
				divisors[num] = divisors[num].union(set([start,end]))
			start += 1
			end = num/start
		# for j in range(num/3,1,-1):
		# 	print j
		# 	if num % j == 0:
		# 		divisors[num] = divisors[num].union(set([j,num/j]))
		i += 1

	# for div,numba in sorted(divisors.items()):
		# print str(div), str(numba)

	return num

print find(450)