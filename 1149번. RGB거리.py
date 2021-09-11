import sys

def main() :
    global hcolor
    n = int(sys.stdin.readline())
    hcolor = []
    
    for i in range(n) :
        hcolor.append(list(map(int,sys.stdin.readline().split())))
    for i in range(1, n) :
        hcolor[i][0] = min(hcolor[i-1][1], hcolor[i-1][2]) + hcolor[i][0]
        hcolor[i][1] = min(hcolor[i-1][0], hcolor[i-1][2]) + hcolor[i][1]
        hcolor[i][2] = min(hcolor[i-1][0], hcolor[i-1][1]) + hcolor[i][2]

    print(min(hcolor[n-1]))
        
if __name__ == "__main__" :
    main()
    
