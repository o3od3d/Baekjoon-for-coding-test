from collections import deque
# 입력
M,N = map(int,input().split())
board = []
for _ in range(N):
    board.append(list(map(int,input().split())))

direction = [[0,1],[0,-1],[-1,0],[1,0]]
cnt = -1e9         # 익는데 걸리는 최소 일수
visited = [[0] * M for _ in range(N)]

# 초기 다 익은 토마토 위치 담기
q = deque()
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            q.append([i, j])
            visited[i][j] = 1

# 덜 익은 토마토 익은 토마토로 바꿔주기
def bfs():
    while q:
        x,y = q.popleft()
        for dir in direction:
            nx = x +dir[0]
            ny = y +dir[1]
            if 0 <= nx <N and 0 <= ny <M:
                if board[nx][ny] == 0:
                    board[nx][ny] = 1
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx,ny])
bfs()
tomato = 0
# visited 배열의 최댓값의 -1이 익는데 걸리는 최소 일 수
for v in visited:
    tmp = max(v)
    cnt = max(cnt,tmp)

# 덜 익은 토마토 개수
for b in board:
    tomato += b.count(0)
# 출력
if tomato == 0:
    print(cnt - 1)
else:
    print(-1)
