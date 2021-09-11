import sys

inf = sys.stdin
ans = 0

alphabet = [ 0 for i in range(26) ]
expression = []

n = int(input())

for i in range(n) :
    expression.append(inf.readline().strip('\n'))

for i in range(n) :
    k = 0 
    for j in range(len(expression[i])-1, -1, -1) :
        alpha = expression[i][j]
        alphabet[ord(alpha) - ord('A')] += pow(10, k)
        k += 1

alphabet.sort(reverse=True)
for i in range(9, -1, -1) :
    ans += i * alphabet[9 - i]

print(ans)
