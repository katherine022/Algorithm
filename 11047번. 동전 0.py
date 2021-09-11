import sys

n,k = map(int, input().split())
coin = []
for i in range(n) :
    coin.append(int(sys.stdin.readline()))

coin.reverse()
num = 0
for i in range(n) :
    num += k // coin[i]
    k %= coin[i] 

print(num)
