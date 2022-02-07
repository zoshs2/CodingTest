import sys
# 가장 높은 차가 그 배열의 난이도가 된다.
# 이 문제는 주어진 리스트를 가장 난이도가 낮은 최적의 배열을 찾고, 그 난이도를 출력하는 문제이다.
# 통나무를 빙 둘러서 배치하기 때문에, 배열의 첫 값과 마지막 값의 차이도 난이도에 기여한다.
# 풀이 방법은 오름차순으로 우선 배열하고, 낮은 수부터 꺼내면서 차례차례 전체 공간의 앞 뒤에 나눠서 배치하면 된다.
# 즉, [1,2,3,4,5,6] 입력데이터에서 이를 수행하면,
# [1,3,5], [6,4,2]으로 나눠지고 최종적으로 [1,3,5,6,4,2]로 배치되게 된다. 이것이 가장 적은 난이도를 가진 최적의 배치다!!!
T = int(input())
answer = []
for _ in range(T):
    LogList = []
    BackLogList = []
    N = int(input())
    for i, height in enumerate(sorted(list(map(int, sys.stdin.readline().strip().split())))):
        if i%2==0:
            LogList.append(height)
        else:
            BackLogList.append(height)
    
    LogList.extend(sorted(BackLogList, reverse=True))
    Diff = []
    for i in range(len(LogList)):
        if i+1 == len(LogList):
            Diff.append(abs(LogList[i]-LogList[0]))
            break
        Diff.append(abs(LogList[i] - LogList[i+1]))

    answer.append(str(max(Diff)))

print("\n".join(answer))