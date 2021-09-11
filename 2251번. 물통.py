import sys
from collections import deque
input = sys.stdin.readline

def bfs(a,b,c) :
    visited = [[[ 0 ] * (water[2]+1)] * (water[1]+1) for _ in range(water[0]+1)]
    deq = deque()
    
    deq.append([a,b,c])
    visited[a][b][c] = 1

    ### 첫번째
    tmp = [ 0, 0, c ]
    if water[2] >= water[0] :
        tmp[0] = water[0]
        tmp[2] = water[2] - water[0]
        #print(tmp)
    else :
        tmp[0] = water[2]
        tmp[2] = 0
    deq.append(tmp)
    visited[tmp[0]][tmp[1]][tmp[2]] = 1

    ### 두번째
    tmp = [0,0, c]
    if water[2] >= water[1] :
        tmp[1] = water[1]
        tmp[2] = water[2] - water[1]
    else :
        tmp[1] = water[2]
        tmp[2] = 0
    deq.append(tmp)
    visited[tmp[0]][tmp[1]][tmp[2]] = 1 
    
    while deq :
        here = deq.popleft()
        #print(here)
        if here[0] == 0 :
            ans[here[2]] = 1
            
        nxt = here.copy()
        for i in range(3) :
            if 0 < here[i] <= water[i] :
                for j in range(3) :
                    if i == j :
                         continue
                    if here[i] + here[j] <= water[j] :
                        nj, ni = here[i]+here[j], 0
                    else :
                        nj, ni = water[j], here[i]+here[j] - water[j]
                    nxt[j] = nj
                    nxt[i] = ni
                    if not visited[nxt[0]][nxt[1]][nxt[2]] :
                        visited[nxt[0]][nxt[1]][nxt[2]] = 1
                        deq.append(nxt)
                    nxt = here.copy()

water = list(map(int, input().split(" ")))
ans = [ 0 for _ in range(water[2]+1) ]

bfs(0,0, water[2])
for i in range(0, water[2]+1) :
    if ans[i] == 1 :
        print(i, end=' ')
