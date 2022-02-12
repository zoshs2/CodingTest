import sys

N, M = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))
neg_arr = []
pos_arr = []
for loc in arr:
    if loc < 0:
        neg_arr.append(abs(loc))
    else:
        pos_arr.append(loc)

neg_max = 0
pos_max = 0
for loc in neg_arr:
    if loc > neg_max:
        neg_max = loc
        
for loc in pos_arr:
    if loc > pos_max:
        pos_max = loc

neg_arr = sorted(neg_arr, reverse=True)
pos_arr = sorted(pos_arr, reverse=True)
temp = []
last_step = []
if neg_max >= pos_max:
    for i in range(len(neg_arr)):
        if i < M:
            last_step.append(neg_arr[i])
        else:
            temp.append(neg_arr[i])
    neg_arr = temp

else:
    for i in range(len(pos_arr)):
        if i < M:
            last_step.append(pos_arr[i])
        else:
            temp.append(pos_arr[i])
    pos_arr = temp

steps = 0
steps += abs(last_step[0])
steps += 2 * (sum(neg_arr[::M]) + sum(pos_arr[::M]))
print(steps)