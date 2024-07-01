""" Example Input
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
Example Out : 200
"""
from collections import Counter
_ = int(input())
shoe_sizes = map(int,input().split())
count_sz = Counter(shoe_sizes)
N = int(input())
cr = [list(map(int,input().split())) for _ in range(N)]
sales = 0

for i in range(N):
    if count_sz[cr[i][0]]:
        sales += cr[i][1]
        count_sz[cr[i][0]] -= 1
print(sales)