from sys import stdin

s = stdin.readline().rstrip()
bomb = stdin.readline().rstrip()
len_bomb = len(bomb)

stack = []
for i in range(len(s)) :
    stack.append(s[i])
    if s[i] == bomb[len_bomb - 1] and len(stack) >= len_bomb:
        cnt = 0
        for j in range(len_bomb) :
            #print(j, len(stack)-1-j, stack[len(stack)-1-j])
            if(stack[len(stack)-len_bomb+j] == bomb[j] ) :
                cnt += 1
        #print(cnt)
        if cnt == len_bomb :
            for j in range(len_bomb) :
                stack.pop()
if len(stack) == 0 :
    print("FRULA")
else :
    print(''.join(stack))
