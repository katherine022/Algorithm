import sys
from collections import deque

def bfs(x,y) :
    visited = [ [0] * M for _ in range(N) ]
    deq = deque()
    deq.append([x,y])
    visited[x][y] = 1

    level = 1
    while deq :
        qSize = len(deq)
        dx = [0,0,1, -1]
        dy = [1,-1,0,0]
        #print(level)
        for _ in range(qSize) :
            here = deq.popleft()
            #print(here)
            if here == [N-1,M-1] :
                return level
            for i in range(4) :
                nx = here[0] + dx[i]
                ny = here[1] + dy[i]
                if 0 <= nx < N and 0 <= ny < M :
                    if not visited[nx][ny] and miro[nx][ny] == 1 :
                        visited[nx][ny] = 1
                        deq.append([nx,ny])
        level+= 1

input = sys.stdin.readline

N,M = map(int, input().split())
miro = [ list(map(int, input().rstrip())) for _ in range(N) ]
print(bfs(0,0))
