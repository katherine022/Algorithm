import sys
from collections import deque

def bfs(w, h, b) :
    global guide
    w_deq = deque(w)
    h_deq = deque()
    visited = [ [0] * C for _ in range(R) ] 

    visited[h[0]][h[1]] = 1
    h_deq.append(h)    
    dx = [0,0,-1, 1]
    dy = [1, -1, 0, 0]
    level = 1
    
    while h_deq :
        hSize = len(h_deq)
        for _ in range(hSize) :
            h_x, h_y = h_deq.popleft()
            if guide[h_x][h_y] == "*" :
                continue
            
            for i in range(4) :
                h_nx = h_x + dx[i]
                h_ny = h_y + dy[i]

                if 0<= h_nx < R and 0 <= h_ny < C :
                    if guide[h_nx][h_ny] == "." and not visited[h_nx][h_ny]:
                        h_deq.append([h_nx, h_ny])
                        visited[h_nx][h_ny] = 1
                    elif guide[h_nx][h_ny] == "D" :
                        return level
        wSize = len(w_deq)
        for _ in range(wSize) :
            w_x, w_y = w_deq.popleft()

            for i in range(4) :
                w_nx = w_x + dx[i]
                w_ny = w_y + dy[i]
                if 0 <= w_nx < R and 0 <= w_ny < C and guide[w_nx][w_ny] == "." :
                    guide[w_nx] = guide[w_nx][ : w_ny] + "*" + guide[w_nx][w_ny+1:]
                    w_deq.append([w_nx,w_ny])
        level += 1
    return -1
input = sys.stdin.readline

R,C = map(int, input().split())
guide = [ input().rstrip() for _ in range(R) ]
water = []

for i in range(R) :
    for j in range(C) :
        if guide[i][j] == "*" :
            water.append([i,j])
        elif guide[i][j] == "S" :
            Hedgehog = [i,j]
        elif guide[i][j] == "D" :
            Beavor = [i,j]

result = bfs(water, Hedgehog, Beavor)
if result == -1 :
    print("KAKTUS")
else :
    print(result)

