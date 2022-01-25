import sys

def solution(scorelist):
    # 통과! 역시 여기서 단일 for문을 써야된다.
    scorelist = sorted(scorelist, key=lambda x: x[0])
    new_score = [score[1] for score in scorelist]
    cnt = 0
    Threshold = new_score[0]
    for i in range(len(new_score)):
        if i == 0:
            cnt += 1
            continue
        if Threshold > new_score[i]:
            cnt += 1
            Threshold = new_score[i]

    return cnt

'''
def solution(scorelist):
    # 시간초과 solution2
    scorelist = sorted(scorelist, key=lambda x: x[0])
    FailedCnt = 0
    Total = len(scorelist)
    for i in range(Total):
        if i == Total - 1:
            FailedCnt += 1
        else:
            for _, i_s in scorelist[:i]:
                if scorelist[i][1] > i_s:
                    FailedCnt += 1
                    break          

    return Total - FailedCnt
'''

'''
def solution(scorelist):
    # 시간초과 solution1
    cnt = 0
    for p_score, i_score in scorelist:
        if p_score == 1 or i_score == 1:
            cnt += 1
        else:
            for comp_p, comp_i in scorelist:
                pFlag = False
                iFlag = False
                if p_score > comp_p:
                    pFlag = True
                if i_score > comp_i:
                    iFlag = True
                if pFlag and iFlag:
                    break
            else:
                if pFlag and iFlag:
                    continue
                else:
                    cnt += 1

    return cnt
'''
if __name__ == '__main__':
    n = int(input())
    answer = []
    for _ in range(n):
        NumStd = int(input())
        ScoreList = []
        for _ in range(NumStd):
            ScoreList.append(list(map(int, sys.stdin.readline().strip().split())))
        result = solution(ScoreList)
        answer.append(result)
    
    for sol in answer:
        print(sol)