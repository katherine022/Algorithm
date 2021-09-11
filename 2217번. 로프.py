import sys

n = int(input())

kg = []
for i in range(n) :
    kg.append(int(sys.stdin.readline()))

kg.sort(reverse=True)
max = kg[0]

for i in range(1, n) :
        if max < kg[i] * (i+1) :
            max = kg[i] * (i+1)

print(max)
