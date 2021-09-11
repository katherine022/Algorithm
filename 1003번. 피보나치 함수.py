fibos = [ [ -1 for i in range(2) ] for i in range(41) ]

def main() :
    T = int(input())

    fibos[0][0] = 1
    fibos[0][1] = 0

    fibos[1][0] = 0
    fibos[1][1] = 1
    
    for i in range(41) :
        if i == 0 or i == 1 :
            continue
        if fibos[i-1][0] == -1 and fibos[i-1][1] == -1 and fibos[i-2][0] == -1 and fibos[i-2][1] == -1 :
            continue
        else :
            fibos[i][0] = fibos[i-1][0] + fibos[i-2][0]
            fibos[i][1] = fibos[i-1][1] + fibos[i-2][1]

    for i in range(T) :
        N = int(input())
        print( fibos[N][0], fibos[N][1])
        
if __name__ == "__main__" :
    main()
