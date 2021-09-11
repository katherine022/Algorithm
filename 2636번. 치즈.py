import sys
from collections import deque

input = sys.stdin.readline

def bfs0(x,y) :
    visited[x][y] = 1
    zero = [[x,y]]
    de = deque()
    de.append([x,y])

    while de :
        he_x, he_y = de.popleft()
        for i in range(4) :
            nx = he_x+ dx[i]
            ny = he_y + dy[i]
            if 0<= nx < n and 0 <= ny < m and not visited[nx][ny] and cheese[nx][ny] == 0 :
                visited[nx][ny] = 1
                zero.append([nx,ny])
                de.append([nx,ny])
    return zero
                
def bfs() :
    one = bfs0(0,0)
    deq = deque(one)
    level = 0
    while deq :
        qSize = len(deq)
        hour[level] = qSize
        zero = deque()
        #print(level, qSize, sorted(deq))
        #print("----------------------------------------------")

        for _ in range(qSize) :
            here_x, here_y = deq.popleft()
            cheese[here_x][here_y] = 0
            #print(qSize, here_x, here_y)

            for i in range(4) :
                nx = here_x + dx[i]
                ny = here_y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    if cheese[nx][ny] == 0 :
                        zero += bfs0(nx,ny)
                    else : 
                        visited[nx][ny] = 1
                        deq.append([nx,ny])
        #print("zero : ", zero)
        while zero :
            here_x,here_y = zero.popleft()

            for i in range(4) :
                nx = here_x + dx[i]
                ny = here_y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] :
                    visited[nx][ny] = 1
                    deq.append([nx,ny])
        level += 1
    return level - 1

n,m = map(int, input().split())
cheese = [ list(map(int, input().split())) for _ in range(n) ]
hour = {}

dx = [ 0, 0, -1, 1]
dy = [ 1, -1, 0, 0]
visited = [ [ 0 ] * m for _ in range(n) ]

ans = bfs()
print(ans)
print(hour[ans])

