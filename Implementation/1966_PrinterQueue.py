from collections import deque

def solution(target_idx, quelist):
    tNum = quelist[target_idx]
    new_list = deque([])
    for i in range(len(quelist)):
        if i == target_idx:
            new_list.append('target')
        else:
            new_list.append(quelist[i])
    
    quelist = deque(quelist)
    order = 1
    while True:
        Max = max(quelist)
        length = len(quelist)
        if Max == tNum:
            break
        for _ in range(length):
            if Max not in quelist:
                break
            
            if quelist[0] == Max:
                quelist.popleft()
                new_list.popleft()
                order += 1
            else:
                quelist.append(quelist.popleft())
                new_list.append(new_list.popleft())

    tIdx = new_list.index('target')
    answer = order + list(new_list)[:tIdx].count(tNum)
    return answer

if __name__ == '__main__':
    NumCase = int(input())
    Answers = []
    for _ in range(NumCase):
        numSample, target = map(int, input().split())
        PriorList = list(map(int, input().split()))
        sol = solution(target, PriorList)
        Answers.append(str(sol))
    
    print("\n".join(Answers))