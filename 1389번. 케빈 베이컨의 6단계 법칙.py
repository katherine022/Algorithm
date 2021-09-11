import sys
from collections import deque
from bisect import bisect_left

def bfs() :
    deq = deque()

    for i in range(1, N+1) :
        visited = [0] * (N+1)
        deq.append(i)
        visited[i] = 1
        level = 0
        #print(i, "번째")
        while deq :
            qSize =len(deq)
            #print("-- level" + str(level) + " --")
            for _ in range(qSize) :
                here = deq.popleft()
                #print(i, here)
                bacon[i][here] = level
                
                for friend in relation[here] :
                    if not visited[friend] :
                        visited[friend] = 1
                        deq.append(friend)
            level += 1
        
                        
input = sys.stdin.readline

N,M = map(int, input().split())
relation = [ [] for _ in range(N+1)]
bacon = [ [0] * (N+1) for _ in range(N+1)]
for _ in range(M) :
    a,b = map(int, input().split())
    
    relation[a].append(b)
    relation[b].append(a)
    #print(a,b, relation)
bfs()

m = min(bacon[1:], key = lambda x : sum(x))

for i in range(1, N+1) :
    if m == bacon[i] :
        print(i)
        break
    



