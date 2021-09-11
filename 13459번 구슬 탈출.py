### 입력 받기 
N,M = map(int,input().split())

board = [] #보드판 
red = [] #빨간 구슬의 위치
blue = [] #파란 구슬의 위치
ans = 0 # 움직이는 횟수
flag = False #빼낼 수 있는지 여부
visited = [0 for i in range(10)] 

for i in range(0, N) :
    tmp = list(input())
    board.append(tmp)
    if 'R' in tmp :
        red.append(i)
        red.append(tmp.index())
    if 'B' in tmp :
        blue.append(i)
        blue.append(tmp.index())

### 보드 움직이기
dx = [ 0, 0, -1, 1] 
dy = [ 1, -1, 0, 0] 

while ans <= 10 :
    for i in range(0, 4) :
        red_x = red[0] + dx
        red_y = red[1] + dy
        blue_x = blue[0] + dx
        blue_y = blue[1] + dy

        ## 빨간 구슬 상하좌우 움직이기 
        while True :
            if board[red_x][red_y] == '#' :
                red_x -= dx
                red_y -= dy
                break
            if board[red_x][red_y] == 'O' :
                break
            red_x += dx
            red_y += dy

        while True :
            if board[blue_x][blue_y] == '#' :
                blue_x -= dx
                blue_y -= dy
                break
            if board[blue_x][blue_y] == 'O' :
                break
            blue_x += dx
            blue_y += dy

        if board[blue_x][blue_y] == 'O' :
            break

        
if flag :
    print(1)
else :
    print(0)

        
    


    

###출력하기 


        
