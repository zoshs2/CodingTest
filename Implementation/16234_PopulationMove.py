import sys
from collections import defaultdict
from collections import deque
from math import floor

# Brutal Force
N, L, R = map(int, sys.stdin.readline().strip().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().strip().split())))

def dfs(matrix, graph, st_node):
    visited = []
    need_visited = deque()
    need_visited.append(st_node)
    
    result = 0
    while need_visited:
        node = need_visited.popleft()
        if node not in visited:
            visited.append(node)
            i, j = map(int, node.split('_'))
            result += matrix[i][j]
            need_visited.extend(graph[node])

    update = floor(result / len(visited))
    for node in visited:
        i, j = map(int, node.split('_'))
        matrix[i][j] = update

    return matrix, visited

days = 0
while True:
    graph = defaultdict(list)
    cond = lambda x: True if L <= x <= R else False
    for i in range(N-1):
        for j in range(N-1):
            diff = abs(matrix[i][j] - matrix[i][j+1])
            if cond(diff):
                graph['_'.join(map(str, [i, j]))].append('_'.join(map(str, [i, j+1])))
                graph['_'.join(map(str, [i, j+1]))].append('_'.join(map(str, [i, j])))
            
            diff = abs(matrix[i][j] - matrix[i+1][j])
            if cond(diff):
                graph['_'.join(map(str, [i, j]))].append('_'.join(map(str, [i+1, j])))
                graph['_'.join(map(str, [i+1, j]))].append('_'.join(map(str, [i, j])))

            
    else:
        for j in range(N-1):
            diff = abs(matrix[N-1][j] - matrix[N-1][j+1])
            if cond(diff):
                graph['_'.join(map(str, [N-1, j]))].append('_'.join(map(str, [N-1, j+1])))
                graph['_'.join(map(str, [N-1, j+1]))].append('_'.join(map(str, [N-1, j])))
        
        for i in range(N-1):
            diff = abs(matrix[i][N-1] - matrix[i+1][N-1])
            if cond(diff):
                graph['_'.join(map(str, [i, N-1]))].append('_'.join(map(str, [i+1, N-1])))
                graph['_'.join(map(str, [i+1, N-1]))].append('_'.join(map(str, [i, N-1])))

    if len(graph) == 0:
        break

    else:
        days += 1
        visited = []
        for k in graph.keys():
            if k in visited:
                continue
            else:
                matrix, visited = dfs(matrix, graph, k)

print(days)