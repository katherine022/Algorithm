from sys import stdin

T = int(stdin.readline().rstrip())
for _ in range(T) :
    N = int(stdin.readline().rstrip())
    phone = []
    for __ in range(N) :
        phone.append(stdin.readline().rstrip())
    isConsist = False

    phone.sort()
    for i in range(N-1) :
        m = len(phone[i]) if len(phone[i]) < len(phone[i+1]) else len(phone[i+1])
        if phone[i][:m] == phone[i+1][:m] :
            isConsist = True
            break
    if isConsist == False :
        print("YES")
    else :
        print("NO")
            
            
