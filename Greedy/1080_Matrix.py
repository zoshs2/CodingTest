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

BoolMatrix = []
for i in range(N):
    BoolMatrix.append([True if ele[0]==ele[1] else False for ele in zip(before[i], after[i])])

new_n = N - 2
new_m = M - 2
if new_n <= 0 or new_m <= 0:
    CheckFC = [ele for row in BoolMatrix for ele in row]
    if sum(CheckFC) != N*M:
        print(-1)
        exit(0)
    else:    
        print(cnt)
        exit(0)

cnt = 0
for i in range(new_n):
    for j in range(new_m):
       if BoolMatrix[i][j] == False:
           BoolMatrix[i][j:j+3] = [not ele for ele in BoolMatrix[i][j:j+3]]
           BoolMatrix[i+1][j:j+3] = [not ele for ele in BoolMatrix[i+1][j:j+3]]
           BoolMatrix[i+2][j:j+3] = [not ele for ele in BoolMatrix[i+2][j:j+3]]
           cnt += 1

CheckFC = [ele for row in BoolMatrix for ele in row]
if sum(CheckFC) != N*M:
    print(-1)
    exit(0)
else:    
    print(cnt)