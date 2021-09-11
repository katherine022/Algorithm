from sys import stdin

visited = dict()

def dfs(n) :
    if visited.get(n) == None : 
        visited[n] = True
    elif visited.get(n) == False : 
        return 0
    elif visited.get(n) == True :
        visited[n] = False

    sum = 0
    while n > 0 :
        value = pow(n % 10, P)
        sum += value
        n = n // 10

    dfs(sum)
    
    
A,P = map(int, stdin.readline().split(" "))

dfs(A)

findT = [ k for k, v in visited.items() if v == True ]
print(len(findT))
