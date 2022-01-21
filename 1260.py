from collections import deque

def bfs(graph, start, visit_info):
    que = deque([start])
    visit_info[start] = True

    while que: # que가 비어있으면 종료
        v = que.popleft()
        # 맥터미널 에서 end와 함께 print출력하면, 꼭 마지막에 % sign이 따라오는데
        # 이것은 python 문제가 아니라, ZSH 또는 Bash behavior때문이라고 한다.
        # 이게 왜 존재하는지는 설명이 안되있지만, Shell파라미터 PROMPT_EOL_MARK설정으로 변경할 수 있다고 한다.
        print(v, end=' ') 
        if isinstance(graph[v], list):
            for neighbor in graph[v]:
                if not visit_info[neighbor]:
                    que.append(neighbor)
                    visit_info[neighbor] = True

# DFS; 재귀함수 버전
def dfs(graph, start, visit_info):
    visit_info[start] = True
    print(start, end=' ')
    if isinstance(graph[start], list):
        for v in graph[start]:
            if not visit_info[v]:
                dfs(graph, v, visit_info)

# DFS; 반복문 버전 
# 일반적으로 공간복잡도(메모리) 및 시간복잡도(CPU-Time) 측면에서 
# 재귀함수보다 반복문이 더 좋다고 한다.
# 대신, 재귀함수를 사용하면 보다시피 신속한 코딩풀이가 가능하다.
def Iterate_dfs(graph, start, visit_info):
    stack = deque([start])
    while stack:
        node = stack.pop()
        if not visit_info[node]:
            print(node, end=' ')
            visit_info[node] = True
            if isinstance(graph[node], list):
                for n in graph[node][::-1]:
                    stack.append(n)
            
            elif graph[node] == 0:
                continue
    

if __name__ == '__main__':
    v, m, start = map(int, input().split())
    graph = [False] + [0] * v
    visited = [False] + [False] * v # Vertex 방문 기록표
    for _ in range(m):
        n1, n2 = map(int, input().split())
        if graph[n1]==0:
            graph[n1] = [n2]
            # 아래 분기가 존재하는 이유는, 이 문제에서 간선은 방향성이 없기 때문이다.
            # 따라서 1 2 가 들어오면, 자동으로 2 1도 말해주는거다.
            # 이후 만약 2 4 가 들어오면, 2의 연결은 [1]로 이미 존재하므로 append하고, 4는 없으므로 =[2]로 초기화해야한다.
            if graph[n2]==0:
                graph[n2] = [n1]
            else:
                graph[n2].append(n1)
            
        else:
            graph[n1].append(n2)
            if graph[n2]==0:
                graph[n2] = [n1]
            else:
                graph[n2].append(n1)

    # 각각의 Vertex 들이 방문할 수 있는 vertex목록을 오름차순으로 정리
    graph = list(map(lambda x: sorted(x) if isinstance(x, list) else x, graph))
    dfs(graph, start, visited[:])
    print()
    Iterate_dfs(graph, start, visited[:])
    print()
    bfs(graph, start, visited[:])