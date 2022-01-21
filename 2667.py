import sys

def dfs(i, j):
    if i < 0 or i >= N or j < 0 or j >= N:
        return
    if graph[i][j] == 0:
        return

    graph[i][j] = 0
    global NumOfBuilding # (비권장) global variable 사용하겠다는 선언; 함수밖에 있는 전역변수 정보를 가져온다. 이 선언과 이후의 연산은 서로 '독립적으로' 수행해야한다. 
    NumOfBuilding += 1
    # NumOfBuilding.append(1)
    dfs(i-1, j)
    dfs(i+1, j)
    dfs(i, j-1)
    dfs(i, j+1)
    return

if __name__ == '__main__':
    N = int(input())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, sys.stdin.readline().rstrip())))
    
    NumOfDanji = 0
    BuildingNumList = []
    for i in range(N):
        for j in range(N):
            NumOfBuilding = 0
            if graph[i][j] == 1:
                dfs(i, j)
                BuildingNumList.append(NumOfBuilding)
                # BuildingNumList.append(sum(NumOfBuilding))
                NumOfDanji += 1
            else:
                continue

    print(NumOfDanji)
    for num in sorted(BuildingNumList):
        print(num)