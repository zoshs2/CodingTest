from collections import deque

# DFS: 재귀함수 풀이
def WhoSenior(start, visit_info):
    while True:
        if visit_info[start] is True:
            break
        visit_info[start] = True
        num = vertices[start-1]
        WhoSenior(num, visit_info)
    
    return sum(visit_info)

if __name__ == '__main__':
    N = int(input())
    vertices = deque([])
    visited = [False] + [False] * N
    for _ in range(N):
        vertices.append(int(input()))
    
    answer = 0
    answer_ith = 0
    for i in range(1, N+1):
        # [:]없이 '리스트변수'자체(visited)를 넘겨주면, local function 안에서 다루는 것은 리스트원형이다. 
        # 단, single variable(e.g. a=1) 같은 경우는 깊게 복사된 변수가 넘어간다.
        # 즉, 같은 원리 및 다른 의도로, 위 DFS WhoSenior 함수에선 궁극적으로 뱉는 리스트가 재귀과정에서 계속 변화해야하기 때문에
        # [:]없이 리스트변수자체(visit_info)를 넘겨줘야 한다.
        result = WhoSenior(i, visited[:])
        if result > answer:
            answer = result
            answer_ith = i
        
    print(answer_ith)