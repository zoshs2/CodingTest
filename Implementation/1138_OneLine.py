import sys
# 첫번째(1)부터 '기억하고 있던 숫자'를 묻는다.
# 그리고 그 숫자를 인덱스로 차례차례 세우면 된다.
# 다만, 이미 누군가 들어간 위치는 index 순서에서 제외시킨다.

# [정리]
# 1. 초기 줄 순서는 [False, False, False, False]로 되어있고, 아직 누가 어디인지 모르는 상태이다.
# 2. 1번(A)한테 물었더니 '2'란다. 그러면 [False, False, A, False] 가 되는거다.
# 3. 2번째(B)한테 물으니 그 역시 '2'라 대답한다. 
#   그러면 이미 들어간 A를 뺀 나머지 리스트([False, False, (A), False])에 기반해서 [False, False, (A), B]가 되는거다.
# 4. 3번째(C)는 0이란다. 그러면 [C, False, (A), (B)]
# 5. 4번째(D)는 1이라 대답할거다. 그러면 [(C), D, (A), (B)]로 순서가 확정된다.

N = int(input())
Memory = list(map(int, sys.stdin.readline().split()))
Line = [False] * N
for i, m in enumerate(Memory):
    cnt = 0
    for j, l in enumerate(Line):
        if cnt == m and l == False:
            Line[j] = str(i+1) # 나중에 출력을 용이하게 str 으로 저장
        elif bool(l) == True: # 값이 이미 들어가있는 곳은 카운트에서 제외시킨다.
            continue
        cnt += 1

print(" ".join(Line))