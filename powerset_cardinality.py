def powerset_cardinality(n):
	# n is number of elements to combine from
	s = [y for y in range(0,n)]
	def powerset(s):
		x = len(s)
		masks = [1 << i for i in range(x)]
		for i in range(1 << x):
			yield list(ss for mask, ss in zip(masks, s) if i & mask)
	return len(list(powerset(s)))

print(powerset_cardinality(7))