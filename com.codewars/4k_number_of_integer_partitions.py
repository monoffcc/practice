def partitions(n):
	# 정렬된 상태로 수열을 만들면 중복없이 수열을 만들수 있다
	# 합이 n인 집합의 개수를 구할때,
	# 그중 2를 앞에 사용하는 경우의 수는, 
	# (n-2)를 2보다 작거나 같은 수로만 만들수 있는 갯수와 같다
    arr=[[0 for _ in range(n+1)] for _ in range(n+1)]
    arr[1][1]=1
#     print(arr[1])
    for i in range(2,n+1):
        for j in range(1,i):
            arr[i][j]=arr[i-j][min(i-j,j)]+arr[i][j-1]
        arr[i][i]=arr[i][i-1]+1
#         print(f'{i}:{arr[i]}')
    
    return arr[n][n]