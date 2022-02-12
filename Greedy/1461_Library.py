import sys

def HowStep(sign_arr):
    steps = 0
    
    return steps


N, M = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))
neg_arr = []
pos_arr = []
for loc in arr:
    if loc < 0:
        neg_arr.append(loc)
    else:
        pos_arr.append(loc)

if N <= M:
    
    print(max(arr))
    exit(0)

rest = arr[:-M]
last_step = max(arr[-M:])

