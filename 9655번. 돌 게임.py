import sys

dp = [ [-1] * 1001 for i in range(2)]
sys.setrecursionlimit(10**6)

def stone(turn, remain) :
    global dp

    if remain == 0 :
        if turn == 1 :
            dp[turn][remain] = 0
            return dp[1][remain]
        else :
            dp[turn][remain] = 1
            return dp[0][remain]

    if remain < 0 :
        if turn == 1 :
            return False
        else :
            return True

    if dp[turn][remain] != -1 :
        return dp[turn][remain]
    
    if turn == 1 :
        dp[1][remain] = stone(0, remain - 1) or stone(0, remain-3)
    else :
        dp[0][remain] = stone(1, remain-1) and stone(1,remain-3)

    return dp[turn][remain]
   
inf = sys.stdin
n = int(inf.readline())

result = stone(1, n)
if result == True :
    print("SK")
else :
    print("CY")



