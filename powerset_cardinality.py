from itertools import combinations, chain

def powerset_cardinality(n):
	# n is number of elements to combine from
	s = [y for y in range(0,n)]

	# thank you Stefan Falk for the powerset function
	def powerset(s):
		x = len(s)
		masks = [1 << i for i in range(x)]
		for i in range(1 << x):
			yield list(ss for mask, ss in zip(masks, s) if i & mask)

	# alternative
	def powerset2(iterable):
		return chain.from_iterable(combinations(list(iterable), r)
			 for r in range(len(s)+1))

	return len(list(powerset2(s)))

print(powerset_cardinality(7))