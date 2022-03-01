### 2021.10.24
### 매직스타
### https://www.acmicpc.net/problem/3967
### skyna
### python3

import sys
tmp=[]

def dfs(cnt) :
    if cnt == 12 :
        #print(tmp)
        for rule in Rules :
            magic_star = [ ord(tmp[i])-ord('A') + 1 for i in rule ]
            if sum(magic_star) != 26 :
                return 0
        for i, (x,y) in enumerate(state) :
            stars[x][y] = tmp[i]
        for star in stars :
            print(''.join(star))
        return 0
    #print(cnt, tmp, len(tmp))
    x,y = state[len(tmp)]
    if stars[x][y] != '.' and stars[x][y] != 'x':
        tmp.append(stars[x][y])
        dfs(cnt+1)
        tmp.pop()
        return 0

    for i in range(0, 12) :
        if not alpha[chr(ord('A')+i)]:
            alpha[chr(ord('A')+i)]= 1
            tmp.append(chr(ord('A')+i))
            dfs(cnt+1)
            tmp.pop()
            alpha[chr(ord('A')+i)]= 0

input = sys.stdin.readline
rules = [[(1, 1), (1,3), (1,5),(1,7)],
         [(0,4), (1, 3), (2,2), (3,1)],
         [(3,1),(3,3),(3,5),(3,7)],
         [(4,4), (3,5), (2,6), (1,7)],
         [(0,4),(1,5),(2,6),(3,7)]]

Rules = [[1,2,3,4],[0,2,5,7],[7,8,9,10],[11,9,6,4],[0,3,6,10]]
state = [(0,4),(1,1),(1,3),(1,5),(1,7),(2,2),(2,6),(3,1),(3,3),(3,5),(3,7),(4,4)]
# alpha = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0}
alpha = { chr(i) : 0 for i in range(ord('A'), ord('A')+12) }
visited = [ 0 for _ in range(13) ]

stars = [ list(input().strip()) for _ in range(5) ]

for x,y in state :
    if stars[x][y] != 'x' and stars[x][y] != '.' :
        alpha[stars[x][y]] = 2
dfs(0)
#tmp = ['F', 'A', 'I', 'D', 'L', 'H', 'E', 'C', 'J', 'B', 'K', 'G']



