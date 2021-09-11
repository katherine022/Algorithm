import sys
from collections import deque
input = sys.stdin.readline

def bfs(n, m) :
    deq = deque()
    visit = [ 0 ] * 10000
    deq.append(( "", n ))
    visit[n] = 1
    while deq :
        menu, here = deq.popleft()
        if here == m :
            return menu

        d = 2 * here % 10000
        s = (here-1) % 10000
        a,b = divmod(here, 1000)
        l = b*10 + a
        a,b = divmod(here, 10)
        r = b*1000 + a

        if not visit[d] : 
            deq.append((menu+"D", d))
            visit[d] = 1
        if not visit[s] :
            deq.append((menu+"S", s))
            visit[s] = 1
        if not visit[l] :
            deq.append((menu+"L", l))
            visit[l] = 1
        if not visit[r] :
            deq.append((menu+"R", r))
            visit[r] = 1

t = int(input())
for _ in range(t) :
    a,b = map(int, input().split())
    print(bfs(a,b))
