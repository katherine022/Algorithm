import sys
from collections import deque

def bfs() :
    global visited, bef
    level = 0
    deq = deque()

    for seed in tomato :
        deq.append(seed)
        visited[seed[0]][seed[1]] = 1

    dx = [ 0, 0, 1, -1 ]
    dy = [ 1, -1, 0, 0 ]
    
    while deq :
        qSize = len(deq)
        #print("level : ", level, deq)
        for _ in range(qSize) : 
            here_x, here_y = deq.popleft()
            #print(here_x, here_y)
            for i in range(4) :
                nx = here_x + dx[i]
                ny = here_y + dy[i]
                if 0 <= nx < N and 0 <= ny < M :
                    if not visited[nx][ny] and box[nx][ny] == 0 :
                        bef[0] += 1
                        box[nx][ny] = 1
                        visited[nx][ny] = 1
                        deq.append([nx,ny])
        level += 1
    return level - 1
                    
input = sys.stdin.readline

M,N = map(int, input().split(" "))
box = [ list(map(int, input().split(" "))) for _ in range(N) ]
visited = [ [0] * M for _ in range(N) ]
t = 0
bef = [ 0, 0, 0 ]
tomato = []

for i in range(N) :
    for j in range(M) :
        if box[i][j] == -1 :
            bef[2] += 1
        if box[i][j] == 1 :
            bef[1] += 1
            tomato.append([i,j])
            

if bef[1] + bef[2] == (M * N) :
    print( 0 )
else :
    t = bfs()
    if (bef[0] + bef[1] + bef[2]) != (M * N) :
        print( -1 )
    else :
        print(t)


