'''
< 그래프 탐색(실버3) >
개구리가 일렬로 놓여 있는 징검다리 사이를 폴짝폴짝 뛰어다니고 있다. 
징검다리에는 숫자가 각각 쓰여 있는데, 이 개구리는 매우 특이한 개구리여서 
어떤 징검다리에서 점프를 할 때는 그 징검다리에 쓰여 있는 수의 배수만큼 
떨어져 있는 곳으로만 갈 수 있다.

이 개구리는 a번째 징검다리에서 b번째 징검다리까지 가려고 한다. 
이 개구리가 a번째 징검다리에서 시작하여 최소 몇 번 점프를 하여 
b번째 징검다리까지 갈 수 있는지를 알아보는 프로그램을 작성하시오.
'''
import sys

def PolJJak(start_idx, gap_list):
    if gap_list[start_idx] % bridge[start_idx]==0:

if __name__ == '__main__':
    N = int(input())
    bridge = list(map(int, sys.stdin.readline().split()))
    start, end = map(int, sys.stdin.readline().split())
    gap = start - end
    gap_list = sorted([g+1 for g in range(gap)], reverse=True)
    bridge = bridge[start-1:end-1]
    
            
    else:
        step = 0 
        time = gap // bridge[start-1]
        for i in range(time):
            jump = i+1


        