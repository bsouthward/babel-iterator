class Babel:
	def __init__(self, size):
		self.current = 0
		self.high = size

	def __iter__(self):
		return self

	def __next__(self):

		def get_alpha(n):
			alphabet = []
			for c in range(0, 2**n):
				alphabet.append(chr(c))
			return alphabet

		def powerset(s):
			x = len(s)
			masks = [1 << i for i in range(x)]
			for i in range(1 << x):
				yield [ss for mask, ss in zip(masks, s) if i & mask]

		if self.current > self.high:
			raise StopIteration
		else:
			library = list(powerset(get_alpha(self.current)))
			self.current += 1
			return library

for b in Babel(2):
	print(b)