n = int(input())

sum = 1
cnt = 0

while True :
    n -= sum 
    if n >= 0 :
        cnt += 1
        sum += 1
    else :
        break
print(cnt)
    
