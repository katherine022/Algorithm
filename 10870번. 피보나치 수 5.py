dp = [ -1 for i in range(21) ] 
dp[0] = 0
dp[1] = 1

def fibo(n) :
    if n == 0 :
        return 0
    if n == 1 :
        return 1
    if dp[n] != -1 :
        return dp[n]
    else : 
        dp[n] = fibo(n-1)+ fibo(n-2)
        return dp[n]

N = int(input())
print(fibo(N))
