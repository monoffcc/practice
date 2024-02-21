def solution(args):
#     print(f'args : {args}')
    def lin_str(i,lin):
        if(lin>=3):
            return str(args[i-lin])+'-'+str(args[i-1])
        elif(lin==2):
            return str(args[i-2])+','+str(args[i-1])
        else:
            return str(args[i-1])
    lin=1
    result=[]
    for i,n in enumerate(args):                
        if i==0:
            continue
        if abs(n-args[i-1])==1:
            lin+=1
        else:
            result.append(lin_str(i,lin))
            lin=1
    else:
        result.append(lin_str(len(args),lin))
#     print(result)
    return ','.join(result)