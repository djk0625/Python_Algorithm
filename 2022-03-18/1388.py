import sys
sys.setrecursionlimit(10**6)

def dfs_right(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    if graph[x][y] == "-":
        graph[x][y] = "O"
        
        dfs_right(x, y-1)
        dfs_right(x, y+1)
        
        return True
    return False

def dfs_bottom(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    if graph[x][y] == "|":
        graph[x][y] = "O"
        
        dfs_bottom(x-1, y)  
        dfs_bottom(x+1, y)
        
        return True
    return False

n, m = map(int, sys.stdin.readline().split())
graph = []

for _ in range(n):
    graph.append(list(sys.stdin.readline()))
    
answer = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == "-":
            dfs_right(i, j)
            answer += 1
        elif graph[i][j] == "|":
            dfs_bottom(i, j)
            answer += 1

print(answer)