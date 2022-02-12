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

negFlag = False
posFlag = False
if len(neg_arr):
    neg_arr = sorted(neg_arr)
    negFlag = True

if len(pos_arr):
    pos_arr = sorted(pos_arr, reverse=True)
    posFlag = True

if negFlag and posFlag:

if len(neg_arr):

rest = arr[:-M]
last_step = max(arr[-M:])

