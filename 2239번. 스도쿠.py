import sys
input = sys.stdin.readline
test_box = [[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)],
        [(0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)],
        [(0, 6), (0, 7), (0, 8), (1, 6), (1, 7), (1, 8), (2, 6), (2, 7), (2, 8)],
        [(3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)],
        [(3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)],
        [(3, 6), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8), (5, 6), (5, 7), (5, 8)],
        [(6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2)],
        [(6, 3), (6, 4), (6, 5), (7, 3), (7, 4), (7, 5), (8, 3), (8, 4), (8, 5)],
        [(6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8)]]

tmp = [ [0] * 9 for _ in range(9) ]
def test() :
    isError = False

    #### 세로로 검사
    for j in range(0, 9) :
        test_visited = [ 0 for _ in range(10) ]
        for i in range(0, 9) :
            num = tmp[i][j]
            if not test_visited[num] :
                test_visited[num] += 1
            else :
                isError = True
                break
        if isError :
            break
    if isError :
        return False

    ### 박스형으로 검사
    for box in test_box :
        test_visited = [ 0 for _ in range(10) ]
        for x, y in box :
            num = tmp[x][y]
            if not test_visited[num] :
                test_visited[num] += 1
            else :
                isError = True
                break
        if isError :
            break
    if isError :
        return False
    return True
def dfs(row, col):
    if row == 9 :
        if test() :
            for t in tmp :
                print(''.join(list(map(str, t))))
            print("--------------------------")
        return 0
    #print(row, col)
    if sudoku[row][col] != 0 :
        tmp[row][col] = sudoku[row][col]
        dfs(row+1, 0) if col == 8 else dfs(row, col+1)
        tmp[row][col] = 0
        return 0
    
    for i in range(1, 10) :
        if not visited[row][i] :
            visited[row][i] += 1
            tmp[row][col] = i
            dfs(row+1, 0) if col == 8 else dfs(row, col+1)
            tmp[row][col] = 0
            visited[row][i] -= 1
            

sudoku = [ list(map(int, list( input().rstrip()))) for _ in range(9) ]
visited = []
for i in range(9) :
    visit = [0] * 10
    for j in range(9) :
        num = sudoku[i][j]
        if num != 0 :
            visit[num] = 1
    visited.append(visit)

dfs(0,0)

