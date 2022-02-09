import sys
from collections import deque

answer = []
T = int(input())
for _ in range(T):
    func_input = list(sys.stdin.readline().strip())
    arr_number = int(input())
    input_list = sys.stdin.readline().strip()[1:-1].split(',')
    if arr_number == 0:
        arr_input = deque()
    else:
        arr_input = deque(map(int, input_list))
    
    # Reverse 시킬 때마다 시간 cost가 많이 소모된다.
    # 따라서, 다 끝나기 전까진 Reverse '여부'만 판단해서 앞에서 빼거나, 뒤에서 뺴거나로 수행한다.
    revFlag = False
    for func in func_input:
        if func == 'R':
            revFlag = not revFlag
        else:
            if len(arr_input) == 0:
                answer.append('error')
                break
            else:
                if revFlag:
                    arr_input.pop()
                else:
                    arr_input.popleft()
                
    else:
        if revFlag: # 최종적으로 앞선 loop 를 모두 돌리고 나서, reverse '여부'를 반영한다.
            arr_input.reverse() 
        
        answer.append('['+','.join(map(str, list(arr_input))) + ']')
            
for ans in answer:
    print(ans)