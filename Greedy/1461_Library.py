import sys

# N, M에는 옮겨야 하는 책 수(N)와 한번에 옮길 수 있는 책의 양(M)이 주어진다.
# 다음 줄에는 N개의 책 위치가 나열되는데, 음수 - 양수로 주어진다.

# 1. 음수와 양수 위치는 서로 구분하여 분류한다.
N, M = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))
neg_arr = []
pos_arr = []
for loc in arr:
    if loc < 0:
        neg_arr.append(abs(loc))
    else:
        pos_arr.append(loc)

# 2. 가장 멀리 있는 책을 마지막으로 가져다 놓고, 퇴근하는게 효율적이기에
# 음수 - 양수 분류에서 각각 멀리있는 책 위치를 찾아낸다.
neg_max = 0
pos_max = 0
for loc in neg_arr:
    if loc > neg_max:
        neg_max = loc
        
for loc in pos_arr:
    if loc > pos_max:
        pos_max = loc

# 3. 이제 가장 멀리있는 책 순서로 각각 sort를 수행하고,
# 가장 멀리있는 책부터 한번에 들 수 있는 책의 양까지 last_step에 따로 분류해서 담는다.
# Note! 가장 멀리있는 책의 위치가 음수-양수에서 모두 같다면, 어느 쪽을 last_step에 넣던 상관없다.
neg_arr = sorted(neg_arr, reverse=True)
pos_arr = sorted(pos_arr, reverse=True)
temp = []
last_step = []
# 음수쪽 위치가 pos_max보다 크다면(같아도 상관없다고 말했다. Note!), 음수 분류쪽에서 M만큼 last_step에 빼놓고, 
# 나머지를 neg_arr로 다시 구성한다.
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
# 이제 나머지는 왔다갔다 가져다놔야할 책이다.
# 이 때 멀리있는 책부터 sort된 분류에서 한번에 들 수 있는 양(M) interval에 위치한 책이
# 결국 소요되는 걸음 수 이다. 갔다가 와야하므로, X2를 해준다.
steps += 2 * (sum(neg_arr[::M]) + sum(pos_arr[::M]))
print(steps)