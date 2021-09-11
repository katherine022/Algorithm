import sys
from collections import deque

n = int(input())

meeting = []
for i in range(n) :
    meeting.append(tuple(map(int, sys.stdin.readline().split())))

meets = sorted(meeting, key = lambda x : (x[1], x[0]))

cnt = 1
endtime = meets[0][1]

for i in range(1, n) :
    if meets[i][0] >= endtime :
        cnt += 1
        endtime = meets[i][1]

print(cnt)

    
    
