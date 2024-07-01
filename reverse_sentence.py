#1. Reverse Words in a Sentence
"""
Sample Input: Python is awesome

Sample Output: awesome is Python
"""

s1 = "Python is awesome"

s1 = s1.split(" ")
print(' '.join(s1[::-1]))
print(' '.join((reversed(s1))))
