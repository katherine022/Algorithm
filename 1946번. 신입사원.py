import sys

t = int(input())

for i in range(t) :
    n = int(input())
    people = []
    for j in range(n) :
        people.append(list(map(int, sys.stdin.readline().split(' '))))
    cnt = 1
    people.sort(key = lambda x:x[0])
    max = people[0][1]
    for i in range(n) :
        if max > people[i][1] :
            cnt += 1
            max = people[i][1]
    print(cnt)
