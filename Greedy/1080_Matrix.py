import sys

N, M = map(int, input().split())
before = [] 
after = []
for i in range(2):
    for _ in range(N):
        if i == 1:
            arr = list(map(int, list(sys.stdin.readline().strip())))
            after.append(list(map(bool, arr)))
            continue
        arr = list(map(int, list(sys.stdin.readline().strip())))
        before.append(list(map(bool, arr)))  

q1, r1 = divmod(M, 3) # 3 by 3 행렬을 좌우로 몇번 서칭할 수 있는지 = 몫과 나머지를 더한 값
new_m = q1 + r1
q2, r2 = divmod(N, 3)
new_n = q2 + r2
if q1 == 0 or q2 == 0: # 만약 N이나 M이 3미만이라서 한번도 서칭할 수 없다면, -1 반환
    sys.exit("-1")

for i in range(new_n):
    for j in range(new_m):
        arr1 = before[i][j:j+3]
        arr2 = after[i][j:j+3]
        
    
