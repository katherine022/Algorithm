from sys import stdin

N = int(stdin.readline())

prime_number = [ 0 for i in range(N+1)]
prime_number[1] = 1

for i in range(2, N+1) :
    if prime_number[i] == 0 :
        #print( (N+1)//i)
        for j in range(2, N+1) :
            mul = i * j
            if mul > N :
                break
            prime_number[mul] = 1
            

cnt = 0
for i in range(2, N+1) : 
    if prime_number[i] == 0 :
        sum = 0
        for j in range(i, N+1) :
            if prime_number[j] == 0 :
                sum += j
                if sum == N :
                    #print(i, sum)
                    cnt += 1
                elif sum > N :
                    break

print(cnt)
                
