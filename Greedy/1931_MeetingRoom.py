import sys
N = int(input())
schedule = []
for _ in range(N):
    s,e = map(int, sys.stdin.readline().split())
    schedule.append([s, e])

# 우선 빨리 끝나는 시간(e) 기준으로 회의를 정렬하는 것이, 뒤이어 많은 회의 기회를 갖고 있으니, 핵심이다.
# 이후 위 sort과정에서 (2, 2), (1, 2) 와 같은 경우는 sort를 피해가기 떄문에,
# 첫 sort 결과를 시작시간(s)에 대해 한번더 sort를 진행해준다.
schedule = sorted(schedule, key=lambda x: [x[1], x[0]])

cnt = 1 # 회의는 input이 있다면 하나라도 존재할 것이고, 위 sort를 거친 후 가장 첫 element가 시작 회의여야 할 것이다.
EndTime = schedule[0][1]
for i in range(1, N):
    if schedule[i][0] >= EndTime: # 이제 sort된 schedule을 " 순차적으로 하나씩 " 불러오면서 EndTime을 업데이트 해주면서 count하면 된다.
        cnt += 1
        EndTime = schedule[i][1]

print(cnt)