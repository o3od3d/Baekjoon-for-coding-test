from collections import deque
# 입력
N,M,V = map(int,input().split())
edge = [[] for _ in range(N+1)]
for _ in range(M):
    e1,e2 = map(int,input().split())
    edge[e1].append(e2)
    edge[e2].append(e1)

# 작은 수부터 탐색 위해 정렬
for i in range(1,N+1):
    edge[i].sort()

q = deque()
visited = [0 for _ in range(N+1)]
visited2 = [0 for _ in range(N+1)]

def bfs(V):
    # 시작 정점 방문 처리
    q.append(V)
    visited[V] = 1
    resultBfs = [V]
    while q:
        vertex = q.popleft()
        # 연결된 정점 중 방문하지 않은 정점 탐색
        for i in edge[vertex]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1
                resultBfs.append(i)
    return resultBfs

# 시작 정점 방문 처리
resultDfs = [V]
def dfs(vertex):
    visited2[vertex] = 1
    # 연결된 정점 중 방문하지 않은 정점 탐색
    for i in edge[vertex]:
        if visited2[i] == 0:
            resultDfs.append(i)
            dfs(i)

# 출력
dfs(V)
print(' '.join(map(str,resultDfs)))
print(' '.join(map(str,bfs(V))))



