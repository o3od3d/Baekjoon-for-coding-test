
# 입력
from collections import deque
N = int(input())
maps = []
for _ in range(N):
    maps.append(list(map(int,input().strip())))
direction = [[-1,0],[1,0],[0,1],[0,-1]]
num = 1         # maps에서 단지 표시를 위해 사용
result = []     # 각 단지에 속하는 집의 수를 담기 위해 사용

# 아직 단지가 정해지지 않은 집 탐색을 위해 maps에서 1의 위치를 찾기
def pos():
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 1:
                x, y = i, j
                break
    return x,y

# 단지를 형성하기 위한 BFS 탐색 함수
def bfs(x,y,num):
    q = deque()
    visited = [[0] * N for _ in range(N)]
    q.append([x,y])
    visited[x][y] = 1
    maps[x][y] = num + 1
    while q:
        x,y = q.popleft()
        for dir in direction:
            nx = x + dir[0]
            ny = y + dir[1]
            if 0 <= nx <N and 0<= ny <N:
                if visited[nx][ny] == 0 and maps[nx][ny] == 1:
                    visited[nx][ny] = 1
                    q.append([nx,ny])
                    maps[nx][ny] = num + 1


while True:
    x,y = pos()
    bfs(x, y, num)

    cnt = 0
    cntRe = 0
    for m in maps:
        cnt += m.count(1)
        cntRe += m.count(num + 1)
    result.append(cntRe)

    # 단지 형성이 끝난 경우 반복 종료
    if cnt == 0:
        result.sort()
        break
    num += 1

# 출력
print(num)
for i in range(len(result)):
    print(result[i])