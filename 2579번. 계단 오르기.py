from sys import stdin

dp = [ [-1,-1, -1] for _ in range(301) ] 
def steps(now, bef) :
    if now <= 0 or now > n :
        return 0
    if dp[now][bef] != -1 :
        return dp[now][bef]
    
    if bef == 0 or bef == 2 :
         dp[now][bef] = max(steps(now-1, 1)+step[now], steps(now-2, 2)+step[now])
    elif bef == 1 :
        dp[now][bef] = steps(now-2, 2) + step[now]

    return dp[now][bef]

n = int(stdin.readline())
step = [0,]
for _ in range(n) :
    step.append(int(stdin.readline()))

print(steps(n, 0))
