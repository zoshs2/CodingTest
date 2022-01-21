import sys
from collections import deque

def bfs(start_x, start_y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # 시작지점으로부터 그래프 속 모든 포인트까지의 최소거리를 맵핑시킨다.
    # deque 최초 선언과 함께 초기화하려면, iterable한 object를 써줘야한다. 
    queue = deque([[start_x, start_y]]) # 여기서 두 개의 괄호는, (x, y)를 하나의 쌍으로 묶어서 한번에 배출하기 위함이다.
    
    while queue:
        x, y = queue.popleft()
        # 상 / 하 / 좌 / 우 탐색
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            # 범위를 넘어가는 경우 패스
            if next_x < 0 or next_x >= N or next_y < 0 or next_y >= M:
                continue
            # 벽에 부딪힌 경우 패스
            if graph[next_x][next_y] == 0:
                continue
            # 위 두 경우 외의 탐색시, 처음 방문한 지역(이 문제 경우 1)만 방문후 
            # 이전 위치에서의 비용에서 1 더하기
            # 최소경로탐색문제를 bfs - queue 자료구조로 접근하는 이유가, 
            # queue자료구조 특성(First In, First Out)을 통해 특정 경로에 '최소'비용을 먼저 선점하여 처리할 수 있기 때문!
            if graph[next_x][next_y] == 1:
                graph[next_x][next_y] = graph[x][y] + 1
                queue.append([next_x, next_y])

    # 처음 시작위치에서의 비용은 1로 다시 초기화
    graph[start_x][start_y] = 1
    return

if __name__=='__main__':
    N, M = map(int, input().split())

    graph = []
    for _ in range(N):
        graph.append(list(map(int, sys.stdin.readline().rstrip())))

    # 최소거리 맵핑을 시작할 지점(인덱스)을 입력값으로 쓴다.
    bfs(0, 0)
    print(graph)
    print(graph[N-1][M-1])