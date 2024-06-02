map = [
    ['1', '1','1','1','1','1'],
    ['e', '0','0','0','0','1'],
    ['1', '0','1','0','1','1'],
    ['1', '1','1','0','0','x'],
    ['1', '1','1','0','1','1'],
    ['1', '1','1','1','1','1'],
]

SIZE = 6

def isvalidpos (r, c) :
    if 0 <= r < SIZE and 0 <= c < SIZE :
        if map[r][c] == '0' or map[r][c] == 'x' :
            return True
        return False

def DFS() :
    print ('DFS : ')
    S = ArrayStack(100)
    S.push((1,0))

    while not S.isEmpty() :
        pos = S.pop()
        print(pos, end = '->')
        (r,c) = pos

        if(map[r][c] == 'x') : # 출구
            return True
        else : 
            map[r][c] ='.' #움직였으면, 움직임을 표시

            if isvalidpos(r-1, c) : S.push((r-1, c)) #상
            if isvalidpos(r+1, c) : S.push((r+1, c)) #하
            if isvalidpos(r, c-1) : S.push((r, c-1)) #좌
            if isvalidpos(r, c+1) : S.push((r, c+1)) #우
        S.display()
    return False

result = DFS()
if result == True :
    print('success')
else :
    print('fail')