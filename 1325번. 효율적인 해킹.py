import sys
from collections import deque

def bfs(start_node) :
    n = 0
    visited = [ False for _ in range(N+1)]
    deq = deque()
    deq.append(start_node)

    visited[start_node] = True
    while deq :
        current = deq.popleft()
        n += 1
        for node in computer[current] : 
            if not visited[node] : 
                visited[node]= True
                deq.append(node)
    return n


N,M = map(int,sys.stdin.readline().split(" "))
computer = { i:[] for i in range(1, N+1) }
for _ in range(M) :
    a,b = map(int,sys.stdin.readline().split(" "))
    computer[b].append(a)

Max = 0
ans = []
for i in range(1, N+1) :
    #print(i)
    tmp = bfs(i)
    if Max < tmp :
        ans = []
        ans.append(i)
        Max = tmp
    elif Max == tmp :
        ans.append(i)
print(' '.join(map(str,ans)))

