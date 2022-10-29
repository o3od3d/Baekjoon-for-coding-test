from collections import deque

# 입력
N,M = map(int,input().split())
board = []
for _ in range(N):
    board.append(list(map(str,input().strip())))

# 빨간, 파란 구슬과 구멍 위치
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            rx,ry = i,j
        elif board[i][j] == 'B':
            bx,by = i,j
        elif board[i][j] == 'O':
            hx,hy = i,j

direction = [[0,1],[0,-1],[1,0],[-1,0]]
q = deque()

# 각 구슬 위치 이동
def move(x,y,dire):
    cnt = 0
    while board[x+dire[0]][y+dire[1]] != '#' and (x != hx or y != hy):
        x += dire[0]
        y += dire[1]
        cnt += 1
    return x,y,cnt

def bfs(rx,ry,bx,by):
    q.append([rx,ry,bx,by,1])
    visited = [[[[0] * M for _ in range(N)] for _ in range(M)]for _ in range(N)]
    visited[rx][ry][bx][by] = 1
    while q:
        rx,ry,bx,by,Tcnt = q.popleft()

        # 10회 초과하여 구슬을 움직일 경우 실패
        if Tcnt > 10:
            print(-1)
            return
        for dir in direction:
            nrx,nry,rcnt = move(rx,ry,dir)
            nbx,nby,bcnt = move(bx,by,dir)

            # 파란 구슬이 구멍으로 들어갈 경우 넘김
            if nbx == hx and nby == hy:
                continue

            # 빨간 구슬이 구멍에 들어갈 경우 성공
            if nrx == hx and nry == hy:
                print(Tcnt)
                return

            # 빨간 구슬과 파란 구슬의 위치가 같을 경우 이동
            if nrx == nbx and nry == nby:
                if rcnt > bcnt:
                    nrx -= dir[0]
                    nry -= dir[1]
                else:
                    nbx -= dir[0]
                    nby -= dir[1]

            # 방문하지 않은 위치인 경우 큐에 넣고 방문 체크
            if visited[nrx][nry][nbx][nby] == 0:
                q.append([nrx,nry,nbx,nby,Tcnt + 1])
                visited[nrx][nry][nbx][nby] = 1
    print(-1)

bfs(rx,ry,bx,by)