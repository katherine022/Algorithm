N = int(input())

sugar = [ 0 for i in range(N+1) ]

for i in range(N+1) :
    if i < 3 or i == 4 :
        continue
    if i == 3 or i == 5 :
        sugar[i] = 1
    elif sugar[i-3] == 0 and sugar[i-5] == 0 :
        continue
    elif sugar[i-3] == 0 :
        sugar[i] = sugar[i-5] + 1
    elif sugar[i-5] == 0:
        sugar[i] = sugar[i-3] + 1
    else :
        sugar[i] = min(sugar[i-5], sugar[i-3]) + 1

if sugar[N] == 0 :
    print(-1)
else :
    print(sugar[N])
    
