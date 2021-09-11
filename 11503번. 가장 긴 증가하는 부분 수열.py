from sys import stdin
import bisect

N = int(stdin.readline().rstrip())
A = list(map(int, stdin.readline().split(" ")))

dp = [ 1 for _ in range(N) ]

for i in range(N) :
    if dp[i] 
    else :
        idx = bisect.bisect_left(dp, A[i])
        print(dp, idx, A[i])
        dp[idx] = A[i]
print(len(dp))
