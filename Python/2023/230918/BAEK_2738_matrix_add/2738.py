N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
arr2 = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        arr[i][j] += arr2[i][j]

for k in range(N):
    print(*arr[k])
