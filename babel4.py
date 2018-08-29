# version that uses itertools
# the previous versions did not have characters repeat, this one will

from itertools import combinations_with_replacement

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

		# Turn result into strings
		def library_to_strings(library, separator=''):
			#return [str.join(l) for l in library]
			results = []
			for l in library:
				for e in l:
					results.append(separator.join(e))
			return results

		# create every possible combination of a set of characters
		def all_combinations(alphabet, n=1):
			results = []
			for i in range(len(alphabet)+1):
				results.append(list(combinations_with_replacement(alphabet, i)))
			return results

		# Do the thing if something isn't broken
		if self.current > self.high:
			raise StopIteration
		else:
			alphabet = get_alphabet(self.current)
			library = library_to_strings(all_combinations(alphabet, self.current))
			self.current += 1
			return library


for b in Babel(2):
	#print(b)
	print(b)