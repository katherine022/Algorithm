import sys
sys.setrecursionlimit(10**6)
def dfs(vertex, depth) :
    visited[vertex] = depth
    isRecur = 0
    if visited[ar[vertex-1]] == 0  :
        isRecur += dfs(ar[vertex-1], depth)
    elif visited[ar[vertex-1]] == depth :
        #print("isCycle with ", vertex, ar[vertex-1])
        isRecur += 1
    return isRecur

def dfs_all() :
    cnt = 1
    recur = 0 
    for i in range(1, N+1) :
        if visited[i] == 0 :
            a = dfs(i, cnt)
        if a > 0 :
            recur += 1
            a = 0
        cnt += 1
    print(recur)

T = int(sys.stdin.readline())
N = 0
ar = []
route = [] 
visited = []

for _ in range(T) :
    N = int(sys.stdin.readline())
    ar = list(map(int, sys.stdin.readline().split(" ")))
    
    route = [ [0] * (N+1) for __ in range(N+1) ]
    visited = [ 0 for __ in range(N+1) ] 
    dfs_all()
