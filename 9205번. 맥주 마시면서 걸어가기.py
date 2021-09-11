import sys
from collections import deque
input = sys.stdin.readline

def route(a, b) :
    return abs(node[a][0] - node[b][0]) + abs(node[a][1] - node[b][1])

t = int(input())
for _ in range(t) :
    n = int(input())
    node = [ list(map(int, input().split())) for __ in range(n+2) ]

    all_route = {}
    for i in range(n+2) :
        tmp = dict()
        for j in range(n+2) :
            if i != j :
                tmp[j] = route(i,j)
            else :
                tmp[i] = 0
        all_route[i] = tmp

    
    isGo = False

    if all_route[0][n+1] <= 1000 :
        print("happy")
    else :
        visited = [0] * (n+3)
        deq = deque()
        deq.append(0)
        visited[0] = 1
        
        while deq :
            here = deq.popleft()
            #print(here)
            
            if here == (n+1) :
                isGo = True
                break
            
            sorted_dict = sorted(all_route[here].items(), key=lambda x : x[1])
            for i in range(n+2) :
                if sorted_dict[i][0] == here :
                    continue
                dest = sorted_dict[i][0]
                way = sorted_dict[i][1]
                #print(i, here, sorted_dict)
                if way <= 1000 and not visited[dest] :
                    #print("visited not", dest, way)
                    deq.append(dest)
                    visited[dest] = 1

        if isGo : print("happy")
        else : print("sad")
