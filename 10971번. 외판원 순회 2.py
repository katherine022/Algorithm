import sys
result = sys.maxsize
def backtracking(start, dest, dist,depth) :
    global visited, result
    visited[dest] = True
    if depth == N :
        if route[dest][first] != 0 :    
            result = min(result, dist + route[dest][first])
        visited[dest] = False 
        return

    for i in range(N) :
        if visited[i] == False and i != first and route[dest][i] != 0 :
            backtracking(dest, i, dist+route[dest][i], depth+1)
    visited[dest] = False 
            
first = 0
N = int(sys.stdin.readline())
visited = [ False for _ in range(N) ]
route = [ list(map(int, sys.stdin.readline().split(" "))) for _ in range(N) ]

for i in range(N) :
    first = i
    backtracking(i,i, 0, 1)

print(result)
