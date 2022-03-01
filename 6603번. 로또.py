### 2021.10.24
### 로또
### https://www.acmicpc.net/problem/6603
### skyna
### python3

import sys
from itertools import combinations
input = sys.stdin.readline

n = 1 
while n != 0 :
    numbers = list(map(int, input().split()))
    n, lottes = numbers[0], numbers[1:]

    getNum = list(combinations(lottes, 6))
    
    for num in getNum :
        print(' '.join(map(str, num)))
    print()
