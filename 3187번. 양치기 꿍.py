import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def dfs(start_x, start_y) :
    global visited, tmp_sheep, tmp_wolf
    
    visited[start_x][start_y] = 1
    if yard[start_x][start_y] == "v" :
        tmp_wolf += 1
    elif yard[start_x][start_y] == "k" :
        tmp_sheep += 1
        
    dx = [ 0, 0, -1, 1]
    dy = [ -1, 1, 0, 0]

    for k in range(4) :
        x = start_x + dx[k]
        y = start_y + dy[k]
        if x >= 0 and x < R and y >= 0 and y < C : 
            if yard[x][y] != "#" and not visited[x][y] :
                dfs(x,y)

a_sheep, a_wolf = 0,0
tmp_sheep, tmp_wolf = 0, 0
R, C = map(int, input().split())
visited = [ [0] * C for _ in range(R) ]
yard = [ list(input()) for _ in range(R) ]

for i in range(R) :
    for j in range(C) :
        if visited[i][j] == 0 and yard[i][j] != "#" :
            dfs(i,j)

            if tmp_wolf < tmp_sheep :
                a_sheep += tmp_sheep
            elif tmp_wolf >= tmp_sheep :
                a_wolf += tmp_wolf
            tmp_wolf, tmp_sheep = 0,0

print( a_sheep, a_wolf )
