def sudoku(puzzle):
    area=[set([1,2,3,4,5,6,7,8,9]) for _ in range(9)] # 3x3 area check
    cols=[set([1,2,3,4,5,6,7,8,9]) for _ in range(9)] # vertical check
    rows=[set([1,2,3,4,5,6,7,8,9]) for _ in range(9)] # horizontal check
    
    def areaNo(i,j):
        return int(i/3)*3+int(j/3)
    
    cnt=0
    for i,row in enumerate(puzzle):
        rows[i]=rows[i].difference(set(row))
        cnt += 9-len(rows[i])
        for j, n in enumerate(puzzle[i]):
            if n==0:
                continue            
            cols[j].remove(n)
            area[areaNo(i,j)].remove(n)

    while cnt<81:
        prev=cnt
        for i in range(9):
            for j in range(9):
                if puzzle[i][j]!=0:
                    continue
                area_no = areaNo(i,j)
                cdd = set([1,2,3,4,5,6,7,8,9])
                cddr = cdd.intersection(rows[i],cols[j],area[area_no])

                if(len(cddr)==1):
                    cnt+=1
                    ans = cddr.pop()
                    rows[i].remove(ans)
                    cols[j].remove(ans)
                    area[area_no].remove(ans)   
                    puzzle[i][j]=ans
#                     print(f'ans:{ans}, ({i},{j}) {cddr}')
        if prev==cnt:
            print(f'cannot find ans')
            break
    return puzzle