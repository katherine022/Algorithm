import sys
from collections import deque

def hide(dest) :
    dist = [0] * 100001
    deq = deque()
    deq.append(dest)

    while deq :
        here = deq.popleft()
        if here == young :
            return dist[here]
        
        if 0 <= (here+1) <= Max and not dist[here+1]  :
            dist[here + 1] = dist[here] + 1
            deq.append(here+1)
            
        if 0 <= (here-1) <= Max and not dist[here-1]   :
            dist[here-1] = dist[here]+1
            deq.append(here-1)
            
        if 0 <= (here*2) <= Max and not dist[here*2] :
            dist[here*2] = dist[here] + 1
            deq.append(here*2)

        
input = sys.stdin.readline
subin, young = map(int, input().split())
Max = 100000
print(hide(subin))
