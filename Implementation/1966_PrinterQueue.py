from collections import deque
def solution(tNum, quelist):
    Max = max(quelist)
    while Max != tNum:
        

if __name__ == '__main__':
    NumCase = int(input())
    Answers = []
    for _ in range(NumCase):
        numSample, target = map(int, input().split())
        PriorList = list(map(int, input().split()))
        tNum = PriorList[target]
        new_list = []
        for i, num in enumerate(PriorList):
            if num > tNum:
                new_list.append('l')
            elif num < tNum:
                new_list.append('s')
            else:
                if i == target:
                    new_list.append('t')
                else:
                    new_list.append('t1')
        order = 1
        new_list = deque(new_list)
        while 'l' in new_list:
            if new_list[0] == 'l':
                new_list.popleft()
                order += 1
            else:
                new_list.append(new_list.popleft())
        
        for i in new_list:
            if 't' == i:
                Answers.append(str(order))
                break

            elif 't1' == i:
                order += 1
            
            else: # 's' 인 경우
                continue
            
    print("\n".join(Answers))