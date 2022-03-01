import sys
from collections import deque
from collections import defaultdict
def bfs() :
    parent = [0] * (N+1)
    visited = [0] * (N+1)
    deq = deque()
    deq.append(1)
    visited[1] = 1

    while deq :
        here =deq.popleft()
        for node in board[here] :
            if not visited[node] :
                parent[node] = here
                visited[node] = 1
                deq.append(node)

    for p in parent[2:] :
        print(p)
    
input = sys.stdin.readline

N = int(input())
board = defaultdict(list)

for _ in range(N-1) :
    a,b = map(int, input().split())
    board[a].append(b)
    board[b].append(a)

bfs()

    
