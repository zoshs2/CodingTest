import sys

def solution(n, lost, reserve):
    PossList = [False] + [True] * n + [True] # 일단 다 가져왔다는 가정에서 출발 
    
    # 차집합 방식이용.
    # lost에 있는 reserve 명단은 제외시키고, set_reserve를 반환하기 위해 집합(set) 연산을 활용했다.
    set_reserve = set(reserve) - set(lost) 
    set_lost = set(lost) - set(reserve)
    
    for noStd in set_lost:
        PossList[noStd] = False
            
    for okStd in set_reserve:  
        if okStd == 1:
            PossList[okStd+1] = True
        else:
            if PossList[okStd-1] == False:
                PossList[okStd-1] = True
            elif PossList[okStd+1] == False:
                PossList[okStd+1] = True
    
    answer = sum(PossList) - 1 # 처음에 Outta range에러 막기위해 조치한 마지막 True 빼줌.
    return answer

if __name__ == '__main__':
    n = int(input())
    lost = list(map(int, sys.stdin.readline().strip().split()))
    reserve = list(map(int, sys.stdin.readline().strip().split()))
    answer = solution(n, lost, reserve)
    print(answer)