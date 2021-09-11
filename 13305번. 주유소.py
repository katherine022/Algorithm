from sys import stdin

n = int(stdin.readline())
road = list(map(int, stdin.readline().split(' ')))
oil = list(map(int, stdin.readline().split(' ')))

min = oil[0]
money = min * road[0]
for i in range(1, n-1) :
    if min * road[i] > oil[i] * road[i] :
        money += oil[i] * road[i]
        min = oil[i]
    else :
        money += min * road[i]

print(money)        
