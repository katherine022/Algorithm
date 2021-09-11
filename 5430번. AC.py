#5430번. AC
#https://www.acmicpc.net/problem/5430
#2021.07.22

import sys
from collections import deque
inf = sys.stdin

T = int(inf.readline())
for _ in range(T) :
    isError = False
    cnt = 0
    p = inf.readline().rstrip()
    n = int(inf.readline().rstrip())
    if n != 0 : 
        ar = deque(inf.readline().rstrip()[1:-1].split(','))
    else :
        ar = inf.readline().rstrip()[1:-1]
        ar = deque()
    
    for menu in p :
        if menu == "R" :
            cnt += 1
        elif menu == "D" :
            if not ar :
                isError = True
                print("error")
                break
            if cnt % 2 == 0 :
                ar.popleft()
            else :
                ar.pop()
    if not isError :
        if cnt % 2 != 0 :
            ar.reverse()
        print("[",end='')
        for i in range(len(ar)) :
            if i == len(ar)-1 :
                print(ar[i],end='')
                break 
            print(ar[i]+",",end='')
        print("]")
