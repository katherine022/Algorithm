from sys import stdin,stdout 

S = list(stdin.readline().rstrip())
T = list(stdin.readline().rstrip())

for _ in range(len(T) - len(S)) :
    a = T.pop()
    if a == "A" :
        continue
    elif a == "B" :
        T = T[::-1]

if T == S :
    print(1)
else :
    print(0)
