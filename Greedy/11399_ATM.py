# 각 사람이 돈을 인출하는데 필요한 시간의 합을 최소로 만드는 프로그램 
import sys

def MinCostSum(CostList):
    CostList = sorted(CostList) # 오름차순으로 정렬
    MinSum = 0
    for i in range(len(CostList)):
        MinSum += sum(CostList[:i+1])
    return MinSum

if __name__ == '__main__':
    N = int(input()) # 사람의 수
    CostMin = list(map(int, sys.stdin.readline().split())) # 각 사람이 인출하는데 걸리는 시간
    answer = MinCostSum(CostMin)
    print(answer)