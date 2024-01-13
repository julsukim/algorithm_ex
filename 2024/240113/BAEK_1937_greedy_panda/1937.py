# NxN 대나무 숲
# 상/하/좌/우 이동
# 새로운 위치는 이전 위치보다 대나무의 갯수가 더 많아야 한다.
# 판다가 최대한 많은 칸을 방문할 수 있는 시작 위치와 이동 경로
# 1 <= N <= 500
# 대나무 갯수 <= 1000000
# 판다의 최대 이동 횟수 출력
from collections import deque
import sys
sys.stdin = open('input.txt')

N = int(input())
forest = [list(map(int, input().split())) for _ in range(N)]

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

print(forest)
max_move = 0

for i in range(N):
    for j in range(N):
        visited = [[0 for _ in range(N)] for _ in range(N)]

        dq = deque()
        start_point = (i, j)
        dq.append(start_point)
        visited[i][j] = 1

        while dq:
            ci, cj = dq.popleft()
            for di, dj in delta:
                ni, nj = ci+di, cj+dj
                if 0 <= ni < N and 0 <= nj < N:
                    if forest[ci][cj] < forest[ni][nj]:
                        visited[ni][nj] = visited[ci][cj] + 1
                        dq.append((ni, nj))
        move = 0
        for i in range(N):
            for j in range(N):
                if move < visited[i][j]:
                    move = visited[i][j]
        if move > max_move:
            max_move = move
            print(visited)

print(max_move)


