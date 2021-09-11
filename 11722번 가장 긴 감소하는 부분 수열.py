from sys import stdin
from bisect import bisect_left

N = int(stdin.readline())
ar = list(map(int, stdin.readline().split(" ")))

dp = [ 1 for _ in range(N) ]

for i in range(N) :
    for j in range(i) :
        if ar[i] < ar[j] :
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
