# DFS + branch cut with cost
def path_finder(area):
    drr = [(0,1),(1,0),(0,-1),(-1,0)]
    trr = list(map(lambda str: list(map(lambda c: int(c),list(str))),area.split('\n')))
    width=len(trr)
    arr= [[-1 for _ in range(width+2)] for _ in range(width+2)]
    for i,t in enumerate(trr):
        arr[i+1][1:-1]=t
    
    print(f'width:{width}')
    cost=[[-1 for _ in range(width+2)] for _ in range(width+2)]
    
    next=[(1,1,0)] #QUEUE (x,y,cost)
    pain=[0]
    while next:
        x,y,p = next.pop(0)
        if(cost[x][y]>=0 and p>=cost[x][y]):
            continue
        
        cost[x][y]=p
        for dx,dy in drr:
            nx=x+dx
            ny=y+dy
            if arr[nx][ny]<0:
                continue
            np=abs(arr[x][y]-arr[nx][ny])+p
            if cost[nx][ny]<0 or cost[nx][ny]>np:                
                next.append((nx,ny,np))
    
    return cost[width][width] # total levels climbed