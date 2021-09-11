import sys
from collections import deque

input = sys.stdin.readline

F,S,G,U,D = map(int, input().split())

visited = [0 for i in range(F+1) ]
deq = deque()
deq.append(S)
visited[S] = 1
level = 0
isGo = False 

while deq :
    qSize = len(deq)

    for _ in range(qSize) :
        here = deq.popleft()
        if here == G :
            isGo = True
            print(level)
            break
        for direct in [ U, -D ] :
            nxt = here + direct
            if 1 <= nxt <= F and not visited[nxt] :
                visited[nxt] = 1
                deq.append(nxt)
    level += 1

if not isGo :
    print("use the stairs")
