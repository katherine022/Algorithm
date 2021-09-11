import sys
from collections import deque

def bfs() :
    deq = deque(ripe_tomato)
    level = 0
    while deq :
        qSize = len(deq)
        for _ in range(qSize) : 
            here_x, here_y, here_z = deq.popleft()

            dx = [ 0, 0, 0, 0, 1, -1 ]
            dy = [ 0, 0, 1, -1, 0, 0 ]
            dz = [ 1, -1, 0, 0, 0, 0 ]

            for i in range(6) :
                nx = here_x + dx[i]
                ny = here_y + dy[i]
                nz = here_z + dz[i]

                if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and tomato[nx][ny][nz] == 0 :
                    tomato_num[0] += 1
                    tomato[nx][ny][nz] = 1
                    deq.append([nx,ny,nz])
        level += 1
    return level - 1
input = sys.stdin.readline

m,n,h = map(int, input().split(" "))
tomato = [ [ list(map(int, input().split())) for _ in range(n) ] for __ in range(h) ]

ripe_tomato = []
tomato_num = [ 0, 0, 0 ] # 0번째는 안익은 토마토 개수, 1번째는 익은 토마토 개수, 2번째는 토마토 없음
for i in range(h) :
    for j in range(n) :
        for k in range(m) :
            if tomato[i][j][k] == 1 :
                ripe_tomato.append([i,j,k])
                tomato_num[1] += 1
            elif tomato[i][j][k] == -1 :
                tomato_num[2] += 1

if sum(tomato_num[1:]) == m*n*h :
    print(0)
else :
    t = bfs()
    if sum(tomato_num) == m*n*h :
        print(t)
    else :
        print(-1)
