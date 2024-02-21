no_range=[(0,1),(1,1),(1,0),(1,-1)]
def validate_battlefield(f1):
    width = len(f1[0])

    # field를 외곽에 0을 입력(range 검사 생략 목적)
    field = [[0 for _ in range(width+2)] for _ in range(width+2)]
    for i,r in enumerate(f1):
        field[i+1][1:len(r)+1] = r
    visit = [[0 for _ in range(width+2)] for _ in range(width+2)]

    # 검사방향 외에 값이 있는지 (대각선 검사 포함)
    def no(x,y,dx,dy):
        for cx,cy in no_range:
            if cx==dx and cy==dy:
                continue
            elif field[x+cx][y+cy]==1:
                print('fail : ',x,y,cx,cy)
                return True
            
    def scan(x,y,dx,dy):
        if(no(x,y,dx,dy)):
            return 10
        
        visit[x][y]=1
        if field[x+dx][y+dy]==1:
            return scan(x+dx,y+dy,dx,dy)+1
        else:
            return 0
        
    result=[0 for _ in range(5)]
    for i in range(1,width+1):
        for j,n in enumerate(field[i]):
            if n==1 and visit[i][j]==0:
                visit[i][j]=1
                length=1
                if field[i][j+1]==1:
                    length+=scan(i,j,0,1)
                elif field[i+1][j]==1:
                    length+=scan(i,j,1,0)
                else:
                    if no(i,j,0,0):
                        return False
                if(length>4):
                    return False
                result[length]+=1
    # print(result)
    return result==[0,4,3,2,1]