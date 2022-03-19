from collections import deque


def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    
    visited = [[0] * m for _ in range(n)]
    visited[x][y] = 1
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            elif visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
                
            elif graph[nx][ny] == 1:
                return visited[nx][ny] - 1
                
n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, 1, -1, -1, 1, -1, 1]

answer = []
for i in range(n):
    for j in range(m):
        if graph[i][j] != 1:
            answer.append(bfs(i, j))
        
print(max(answer))