"""
project euler problem 13

finding the sum of a hugemongous number
"""

sum = 0

f = open('13_numberlist.txt')

for line in f.read().splitlines():
	# print line
	sum += int(line)

print str(sum)[:10]