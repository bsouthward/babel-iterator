class Babel:
	def __init__(self, size):
		self.current = 0
		self.high = size

	def __iter__(self):
		return self

	def __next__(self):
		# A couple helper functions
		# This one generates an 'alphabet'
		def get_alpha(n):
			alphabet = []
			for c in range(0, 2**n):
				alphabet.append(chr(c))
			return alphabet

		# And I defined a powerset function instead of using itertools
		# to keep the class self-contained
		def powerset(s):
			x = len(s)
			masks = [1 << i for i in range(x)]
			for i in range(1 << x):
				yield [ss for mask, ss in zip(masks, s) if i & mask]

		# Do the thing if something isn't broken
		if self.current > self.high:
			raise StopIteration
		else:
			library = list(powerset(get_alpha(self.current)))
			self.current += 1
			return library

# Even just n = 2 results in a pretty big combinatorial space!
for b in Babel(2):
	print(b)