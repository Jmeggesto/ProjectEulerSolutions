#First solution: using itertools

from itertools import permutations

sorted_lexicographic_permutations = sorted([''.join(permutation) for permutation in permutations("0123456789")])
print(sorted_lexicographic_permutations[999999])


#Second solution: hand-built permutation algorithm