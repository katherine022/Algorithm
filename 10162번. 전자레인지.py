times = [300, 60, 10]

T = int(input())

if T % 10 != 0 :
    print(-1)
else :
    for i in range(3) :
        print(T // times[i], end=' ')
        T %= times[i]
