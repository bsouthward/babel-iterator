# version that uses itertools

from itertools import permutations, chain

class Babel:
	# Even just size = 2 results in a pretty big list!
	def __init__(self, size):
		self.current = 0
		self.high = size

	def __iter__(self):
		return self

	def __next__(self):
		# A couple helper functions
		# This one generates an 'alphabet'
		def get_alphabet(n):
			# setting to 65 for testing purposes so it starts at 'a'
			offset = 65
			return [chr(c+offset) for c in range(0, 2**n-1)]

		# Cool powerset implementation from some StackOverflow user
		def powerset(s):
			x = len(s)
			masks = [1 << i for i in range(x)]
			for i in range(1 << x):
				yield list(ss for mask, ss in zip(masks, s) if i & mask)

		# Python docs' recommended implementation using itertools
		# Let's benchmark these eventually!
		def powerset2(iterable):
			s = list(iterable)
			return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

		# Do the thing if something isn't broken
		if self.current > self.high:
			raise StopIteration
		else:
			pset = powerset(get_alphabet(self.current))
			library = [list(permutations(p)) for p in pset]
			self.current += 1
			return library

# Turn result into strings
def library_to_strings(library, separator=''):
	#return [str.join(l) for l in library]
	results = []
	for l in library:
		for e in l:
			separator = ''
			results.append(separator.join(e))
	return results

for b in Babel(2):
	#print(b)
	print(library_to_strings(b))