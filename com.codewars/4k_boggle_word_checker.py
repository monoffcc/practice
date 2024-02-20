def find_word(board, word):  
    
    height = len(board)
    width=len(board[0])
    nord=[] # alphabet to number ('A' -> 0)
    for n in word:
        nord.append(ord(n)-ord('A'))

    poss = [set() for _ in range(26)] # x,y location of each alphabet character
    for i in range(height):
        for j in range(width):
            c=board[i][j]
            n=ord(c)-ord('A')            
            poss[n].add((i,j))
    def search(x,y,p):
        if p>=len(nord):
            return True 
        next = nord[p]        
#         print(f'{x},{y} - {p} {next}')

        for (cx,cy) in poss[next]:
            if abs(x-cx)<2 and abs(y-cy)<2:
                poss[next].remove((cx,cy))
                if(search(cx,cy,p+1)):
                    return True     
                poss[next].add((cx,cy))
        else:
            return False
#     print(f'nord={nord}')
  
    for (x,y) in poss[nord[0]]:
        if(search(x,y,1)):
            return True
    else:
        return False
    
