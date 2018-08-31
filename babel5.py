# version that uses itertools
# the previous versions did not have characters repeat, this one will

from itertools import combinations_with_replacement, permutations
import sys

args = sys.argv

class Babel:
	# works with much smaller n values to give arbitrary list length
	def __init__(self, size, start=0):
		# make args integers
		size, start = int(size), int(start)

		# holds current state of iterator as it counts up from start to size
		if size >= start:
			self.current = start
			self.high = size
		else:
			raise StopIteration

	def __iter__(self):
		return self

	def __next__(self):
		# A couple helper functions
		# This one generates an 'alphabet'
		def get_alphabet(n):
			# setting to 64 for testing purposes so it starts at 'a'
			offset = 64
			alphabet_size = offset + int(n)
			# n defines how many bits the alphabet space is
			return [chr(c+offset) for c in range(1, n+1)]

		# create every possible combination of a set of characters
		def all_combinations(alphabet, n=1):
			return [combinations_with_replacement(alphabet, i)
				 for i in range(len(alphabet)+1)]
		
		# Turn result into array of strings
		def library_to_strings(library, separator=''):
			results = []
			for l in library:
				for e in l:
					results.append(separator.join(e))
			return results

		# version using tuples for speed
		# doesn't quite work yet
		def library_to_strings2(library, separator=''):
			results = ()
			for l in library:
				for e in l:
					results += tuple(separator.join(e))
			return results

		# we also need every permutation
		# takes an array of strings, splits each, and spits out an array of permutations
		def all_permutations(strings):
			perms = []
			for s in strings:
				perms.append(tuple(permutations(s)))
			return perms

		# build the library until the iterator hits its max size
		if self.current > self.high:
			raise StopIteration
		else:
			alphabet = get_alphabet(self.current)
			library = sorted(set(library_to_strings(all_permutations(
				library_to_strings(all_combinations(alphabet, self.current))))))
			self.current += 1
			return library

# print the first few Library of Babel rooms
#for b in Babel(7):
#	print(b)
if len(args) == 3:
	b = Babel(args[1], args[2])
elif len(args) == 2:
	b = Babel(args[1])
else:
	b = Babel(input("Size of library: "), input("Starting point: "))

print(list(b))